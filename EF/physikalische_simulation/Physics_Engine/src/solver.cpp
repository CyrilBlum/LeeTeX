#include "solver.h"
#include "particle.h"
#include <SFML/System/Vector2.hpp>
#include <SFML/System/Vector3.hpp>
#include <cmath>

Solver::Solver(sf::Vector2f constraint_center, float constraint_radius,
               sf::Vector2f a_gravity, unsigned int n_sub_steps, float frame_dt)
    : constraint_center(constraint_center),
      constraint_radius(constraint_radius),
      a_gravity(a_gravity),
      n_sub_steps(n_sub_steps),
      frame_dt(frame_dt) {}

Particle &Solver::add_particle(sf::Vector2f y0, sf::Vector2f v0,
                               sf::Vector2f a0, float radius, sf::Color color) {
    return particles.emplace_back(y0, v0, a0, radius, color);
}

sf::Vector3f Solver::get_constraints() const {
    return {constraint_center.x, constraint_center.y, constraint_radius};
}

const std::vector<Particle> &Solver::get_particles() const { return particles; }

unsigned int Solver::get_particle_count() const { return particles.size(); }

float Solver::get_time() const { return time; }

void Solver::all_updates() {
    time += h;
    for (unsigned int step = 0; step < n_sub_steps; ++step) {
        handle_collisions();
        enforce_constraints();
        verlet_updates(h);
    }
}

void Solver::handle_collisions() {
    const float response_coef = 0.75f;
    const unsigned int particle_count = particles.size();

    for (unsigned int i = 0; i < particle_count; ++i) {
        Particle &particle_1 = particles[i];
        for (unsigned int j = i + 1; j < particle_count; ++j) {
            Particle &particle_2 = particles[j];
            const sf::Vector2f vec_p1p2 =
                particle_1.y_particle - particle_2.y_particle;
            const float squared_dist =
                vec_p1p2.x * vec_p1p2.x + vec_p1p2.y * vec_p1p2.y;
            const float min_dist = particle_1.radius + particle_2.radius;
            if (squared_dist < min_dist * min_dist) {
                const float dist = sqrt(squared_dist);
                const sf::Vector2f vec_p1p2_normalized = vec_p1p2 / dist;
                const float sum_mass = particle_1.radius + particle_2.radius;
                const float mass_ratio_1 = particle_1.radius / sum_mass;
                const float mass_ratio_2 = particle_2.radius / sum_mass;
                const float kappa = 0.5f * response_coef * (dist - min_dist);
                particle_1.y_particle -=
                    vec_p1p2_normalized * mass_ratio_2 * kappa;
                particle_2.y_particle -=
                    vec_p1p2_normalized * mass_ratio_1 * kappa;
            }
        }
    }
}

void Solver::enforce_constraints() {
    for (auto &particle : particles) {
        const sf::Vector2f vec = constraint_center - particle.y_particle;
        const float dist = sqrt(vec.x * vec.x + vec.y * vec.y);
        if (dist > constraint_radius - particle.radius) {
            const sf::Vector2f vec_normalized = vec / dist;
            particle.y_particle =
                constraint_center -
                vec_normalized * (constraint_radius - particle.radius);
        }
    }
}

void Solver::verlet_updates(float h) {
    for (auto &particle : particles) {
        particle.single_verlet_step(h);
    }
}
