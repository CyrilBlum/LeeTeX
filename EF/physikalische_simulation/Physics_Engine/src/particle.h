#ifndef PARTICLE_H_
#define PARTICLE_H_

#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Color.hpp>
#include <SFML/System/Vector2.hpp>

class Particle {
    public:
        Particle(sf::Vector2f y0, sf::Vector2f v0, sf::Vector2f a0,
                 const float radius, sf::Color color);

        void single_verlet_step(float h);

        sf::Vector2f y_particle;
        sf::Vector2f v_particle;
        sf::Vector2f a_particle;
        // needed in case of non-constant acceleration:
        // sf::Vector2f a_particle_new;
        const float radius;
        const sf::Color color = sf::Color::Blue;

    private:
};

#endif // !PARTICLE_H_
