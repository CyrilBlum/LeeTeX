#ifndef SOLVER_H_
#define SOLVER_H_
#include "particle.h"
#include <SFML/System/Vector2.hpp>
#include <SFML/System/Vector3.hpp>
#include <vector>
class Solver
{
public:
  Solver (sf::Vector2f constraint_center, float constraint_radius, sf::Vector2f a_gravity, unsigned int n_sub_steps, float frame_dt);

  Particle &add_particle (sf::Vector2f y0, sf::Vector2f v0, sf::Vector2f a0, float radius, sf::Color color);
  sf::Vector3f get_constraints () const;
  const std::vector<Particle> &get_particles () const;
  unsigned int get_particle_count () const;
  float get_time () const;

  void all_updates ();

private:
  void handle_collisions ();
  void enforce_constraints ();
  void verlet_updates (float h);

  const sf::Vector2f constraint_center;
  const float constraint_radius;
  const sf::Vector2f a_gravity;
  const unsigned int n_sub_steps;
  const float frame_dt;
  const float h = frame_dt / n_sub_steps;
  float time = 0.0f;
  std::vector<Particle> particles;
};

#endif // !SOLVER_H_
