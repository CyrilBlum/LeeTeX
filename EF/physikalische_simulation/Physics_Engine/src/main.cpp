#include "init_window.h"
#include "renderer.h"
#include "solver.h"
#include <SFML/Graphics/RenderWindow.hpp>
#include <cmath>
#include <iostream>
#include <string>
int
main ()
{
  unsigned int width = 800;
  unsigned int height = 1000;
  std::string title = "cool window";
  unsigned int max_fps = 60;
  unsigned int antialiasing_level = 3;
  sf::RenderWindow mywindow;
  init_window (mywindow, width, height, title, max_fps, antialiasing_level);
  Renderer myrenderer{ mywindow };

  const sf::Vector2 constraint_center{ width * 0.5f, height * 0.5f };
  const float constraint_radius = 450.0f;
  const sf::Vector2 a_gravity{ 0.0f, 10.0f };
  const unsigned int n_sub_steps = 8;
  const unsigned int frame_rate = 60;
  Solver mysolver (constraint_center, constraint_radius, a_gravity, n_sub_steps, 1.0f / frame_rate);

  // Set simulation attributes
  const float particle_spawn_delay = 0.40f;
  const float particle_spawn_speed = 100.0f;
  const sf::Vector2f y0 = { 500.0f, 200.0f };
  const sf::Vector2f v0 = { 1.0f, 1.0f };
  const sf::Vector2f a0 = a_gravity;
  const float particle_min_radius = 1.0f;
  const float particle_max_radius = 20.0f;
  const unsigned int max_particles_count = 1000;
  const float max_angle = 1.0f;

  sf::Clock clock;
  // Main loop
  while (mywindow.isOpen ())
    {
      sf::Event event{};
      while (mywindow.pollEvent (event))
        {
          if (event.type == sf::Event::Closed || sf::Keyboard::isKeyPressed (sf::Keyboard::Escape))
            {
              mywindow.close ();
            }
        }

      if (mysolver.get_particle_count () < max_particles_count && clock.getElapsedTime ().asSeconds () >= particle_spawn_delay)
        {
          clock.restart ();
          mysolver.add_particle (y0, v0, a0, particle_max_radius, sf::Color::Green);
          const float t = mysolver.get_time ();
          const float angle = max_angle * std::sin (t) + M_PI * 0.5f;
        }
      mysolver.all_updates ();
      mywindow.clear (sf::Color::White);
      myrenderer.render (mysolver);
      mywindow.display ();
    }

  return 0;
}
