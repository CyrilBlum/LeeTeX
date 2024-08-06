#include "particle.hpp"
#include <SFML/System/Vector2.hpp>
Particle::Particle (sf::Vector2f current_position_, float radius_)
    : last_position{ current_position_ }, current_position{ current_position_ }, acceleration{ 0.0f, 0.0f }, radius{ radius_ }
{
}

void
Particle::verlet_step (float Dt)
{
  // x_{n+1} = 2*x_n - x_{n-1} + A(x_n)*(Dt)^2
  current_position = 2.0f * current_position - last_position + acceleration * Dt * Dt;
  // update the last (previous) position
  last_position = current_position;
}

void
Particle::accelerate (sf::Vector2f a)
{
  acceleration += a;
};

void
Particle::set_velocity (sf::Vector2f v, float Dt)
{
  last_position = current_position - v * Dt;
}

void
Particle::add_velocity (sf::Vector2f v, float Dt)
{
  last_position -= v * Dt;
}

[[nodiscard]] sf::Vector2f
Particle::get_velocity (float Dt) const
{
  return (current_position - last_position) / Dt;
}
