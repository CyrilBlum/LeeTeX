#ifndef INIT_WINDOW_H_
#define INIT_WINDOW_H_
#include <SFML/Graphics.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <string>

sf::RenderWindow &init_window(sf::RenderWindow &window, unsigned int width,
                              unsigned int height, std::string title,
                              unsigned int max_fps,
                              unsigned int antialiasing_level);

#endif // !INIT_WINDOW_H_
