#pragma once

#include "particle.hpp"
#include <SFML/System/Vector2.hpp>
#include <vector>
class Solver
{
public:
  Solver () = default;
  Solver (Solver &&) = default;
  Solver (const Solver &) = default;
  Solver &operator= (Solver &&) = default;
  Solver &operator= (const Solver &) = default;
  ~Solver ();

  Particle &add_particle (sf::Vector2f current_position, float radius);

  void update ();

  void set_simulation_update_rate (unsigned int rate);

  void set_constraint (sf::Vector2f current_position, float radius);

  void set_sub_step_count (unsigned int sub_steps_);

  void set_particle_velocity (Particle &particle, sf::Vector2f v);

  [[nodiscard]] const std::vector<Particle> &get_particles () const;

  [[nodiscard]] sf::Vector3f get_constraint () const;

  [[nodiscard]] unsigned int get_particle_count () const;

  [[nodiscard]] float get_time () const;

  [[nodiscard]] float get_step_Dt () const;

  void apply_gravity ();

  void handle_collisions ();

  void enforce_constraint ();

  void update_particles (float Dt);

private:
  unsigned int sub_steps = 1;
  sf::Vector2f gravity = { 0.0f, 1000.0f };
  sf::Vector2f constraint_center;
  float constraint_radius = 100.0f;
  std::vector<Particle> particles;
  float time = 0.0f;
  float frame_Dt = 0.0f;
};
