#pragma once
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Color.hpp>
#include <SFML/System/Vector2.hpp>

class Particle
{
public:
  Particle (sf::Vector2f current_position_, float radius_);
  Particle () = default;
  Particle (Particle &&) = default;
  Particle (const Particle &) = default;
  Particle &operator= (Particle &&) = default;
  Particle &operator= (const Particle &) = default;
  ~Particle () = default;

  void verlet_step (float Dt);

  void accelerate (sf::Vector2f a);

  void set_velocity (sf::Vector2f v, float Dt);

  void add_velocity (sf::Vector2f v, float Dt);

  [[nodiscard]] sf::Vector2f get_velocity (float Dt) const;

  sf::Vector2f last_position;
  sf::Vector2f current_position;
  sf::Vector2f acceleration;
  float radius;
  sf::Color color;

private:
};
