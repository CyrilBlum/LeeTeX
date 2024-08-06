#include "init_window.hpp"
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/Window/WindowStyle.hpp>
int
main (void)
{
  // create the window
  sf::RenderWindow window;
  init_window (window, 1000, 1000, "mytitle", 60, 1);

  // run the program as long as the window is open
  while (window.isOpen ())
    {
      // check all the window's events that were triggered since the last iteration of the loop
      sf::Event event;
      while (window.pollEvent (event))
        {
          // "close requested" event: we close the window
          if (event.type == sf::Event::Closed)
            window.close ();
        }

      // clear the window with black color
      window.clear (sf::Color::Black);

      // draw everything here...
      // window.draw(...);

      // end the current frame
      window.display ();
    }

  return 0;
}
