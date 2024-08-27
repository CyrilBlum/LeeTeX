#ifndef RENDERER_H_
#define RENDERER_H_

#include "solver.h"

class Renderer
{
public:
  explicit Renderer (sf::RenderTarget &target) : target{ target } {}

  void
  render (const Solver &solver) const
  {
    // Render constraint
    const sf::Vector3f constraint = solver.get_constraints ();
    sf::CircleShape constraint_background{ constraint.z };
    constraint_background.setOrigin (constraint.z, constraint.z);
    constraint_background.setFillColor (sf::Color::Black);
    constraint_background.setPosition (constraint.x, constraint.y);
    constraint_background.setPointCount (128);
    target.draw (constraint_background);

    // Render objects
    sf::CircleShape circle{ 1.0f };
    circle.setPointCount (32);
    circle.setOrigin (1.0f, 1.0f);
    const auto &particles = solver.get_particles ();
    for (const auto &particle : particles)
      {
        circle.setPosition (particle.y_particle);
        circle.setScale (particle.radius, particle.radius);
        circle.setFillColor (particle.color);
        target.draw (circle);
      }
  }

private:
  sf::RenderTarget &target;
};

#endif // !RENDERER_H_
