#include "solver.hpp"
#include "particle.hpp"
#include <SFML/System/Vector2.hpp>
#include <cmath>

Particle &
Solver::add_particle (sf::Vector2f current_position, float radius)
{
  return particles.emplace_back (current_position, radius);
}

void
Solver::update ()
{
  time += frame_Dt;
  for (unsigned int steps{ sub_steps }; --steps;)
    {
      apply_gravity ();
      handle_collisions ();
      enforce_constraint ();
      update_particles (get_step_Dt ());
    }
}

void
Solver::set_simulation_update_rate (unsigned int rate)
{
  frame_Dt = 1.0f / rate;
}

void
Solver::set_constraint (sf::Vector2f current_position, float radius)
{
  constraint_center = current_position;
  constraint_radius = radius;
}

void
Solver::set_sub_step_count (unsigned int sub_steps_)
{
  sub_steps = sub_steps_;
}

void
Solver::set_particle_velocity (Particle &particle, sf::Vector2f v)
{
  particle.set_velocity (v, get_step_Dt ());
}

[[nodiscard]] const std::vector<Particle> &
Solver::get_particles () const
{
  return particles;
}

[[nodiscard]] sf::Vector3f
Solver::get_constraint () const
{
  return { constraint_center.x, constraint_center.y, constraint_radius };
}

[[nodiscard]] unsigned int
Solver::get_particle_count () const
{
  return particles.size ();
}

[[nodiscard]] float
Solver::get_time () const
{
  return time;
}

[[nodiscard]] float
Solver::get_step_Dt () const
{
  return frame_Dt / sub_steps;
}

void
Solver::apply_gravity ()
{
  for (auto &particle : particles)
    {
      particle.accelerate (gravity);
    }
}

void
Solver::handle_collisions ()
{
  const float response_coef = 0.75f;
  const unsigned int particle_count = particles.size ();

  for (unsigned int i{ 0 }; i < particle_count; ++i)
    {
      Particle &particle_1 = particles[i];

      for (unsigned int j{ i + 1 }; j < particle_count; ++j)
        {
          Particle &particle_2 = particles[j];
          const sf::Vector2f vec_p1p2 = particle_1.current_position - particle_2.current_position;
          const float current_squared_dist = vec_p1p2.x * vec_p1p2.x + vec_p1p2.y * vec_p1p2.y;
          const float min_dist = particle_1.radius + particle_2.radius;

          if (current_squared_dist < min_dist * min_dist)
            {
              const float dist = sqrt (current_squared_dist);
              const sf::Vector2f vec_p1p2_normalized = vec_p1p2 / dist;
              const float sum_mass = particle_1.radius + particle_2.radius;
              const float mass_ratio_1 = particle_1.radius / sum_mass;
              const float mass_ratio_2 = particle_2.radius / sum_mass;

              const float kappa = 0.5f * response_coef * (dist - min_dist);

              particle_1.current_position -= vec_p1p2_normalized * mass_ratio_2 * kappa;
              particle_2.current_position -= vec_p1p2_normalized * mass_ratio_1 * kappa;
            }
        }
    }
}

void
Solver::enforce_constraint ()
{
  for (auto &particle : particles)
    {
      const sf::Vector2f vec = constraint_center - particle.current_position;
      const float dist = sqrt (vec.x * vec.x + vec.y * vec.y);
      if (dist > constraint_radius - particle.radius)
        {
          const sf::Vector2f vec_normalized = vec / dist;
          particle.current_position = constraint_center - vec_normalized * (constraint_radius - particle.radius);
        }
    }
}

void
Solver::update_particles (float Dt)
{
  for (auto &particle : particles)
    {
      particle.verlet_step (Dt);
    }
}
