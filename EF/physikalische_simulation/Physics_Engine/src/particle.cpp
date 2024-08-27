#include "particle.h"
#include <SFML/Graphics/Color.hpp>
#include <SFML/System/Vector2.hpp>

Particle::Particle (sf::Vector2f y0, sf::Vector2f v0, sf::Vector2f a0, float radius, sf::Color color)
    : y_particle (y0), v_particle (v0), a_particle (a0), radius (radius), color (color)
{
}

void
Particle::single_verlet_step (const float h)
{
  // step 1: compute y_{k+1}
  y_particle = y_particle + h * v_particle + h * h * a_particle / 2.0f;
  // step 2: in general: derive a_{k+1} from y_{k+1} but here the acceleration is constant
  // (we update the positions rather than have a force act upon the particle)
  // a_particle_new = F(y_{k+1}) / m;
  // step 3: compute v_{k+1}
  // the general verlet step for v_{k+1} would be:
  // v_particle = v_particle + h / 2.0f * (a_particle + a_particle_new);
  // but here the acceleration is constant (a_particle = a_particle_new at all times):
  v_particle = v_particle + h * a_particle;
}
