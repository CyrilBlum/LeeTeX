#include "init_window.h"
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/Window/WindowStyle.hpp>

sf::RenderWindow &init_window(sf::RenderWindow &window, unsigned int width,
                              unsigned int height, std::string title,
                              unsigned int max_fps,
                              unsigned int antialiasing_level) {
    sf::ContextSettings settings;
    settings.antialiasingLevel = antialiasing_level;
    window.create(sf::VideoMode(width, height), title, sf::Style::Default,
                  settings);
    window.setFramerateLimit(max_fps);

    return window;
}
