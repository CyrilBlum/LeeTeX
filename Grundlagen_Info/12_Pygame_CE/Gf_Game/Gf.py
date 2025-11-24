import pygame
import os

from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

pygame.display.set_caption("Space Shooter")

# surface
surf = pygame.Surface((100, 200))
surf.fill("orange")

# image path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "..", "Project_Files", "Space_Shooter", "images")

# player
player_surf = pygame.image.load(image_path + "/player.png").convert_alpha()
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = 1

# meteor
meteor_surf = pygame.image.load(image_path + "/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_surf = pygame.image.load(image_path + "/laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# stars
star_surf = pygame.image.load(image_path + "/star.png").convert_alpha()
star_positions = [
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)
]

# game loop
while running:
    clock.tick(24)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    player_rect.x += player_direction * 100
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1

    display_surface.blit(player_surf, player_rect)

    # update the game
    pygame.display.update()

# exit pygame
pygame.quit()
