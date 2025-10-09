import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
icon = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/icon.png")
pg.display.set_caption("Kollisions-Game")
pg.display.set_icon(icon)

background_color = (50, 80, 120)

player = pg.Rect(WIDTH // 2 - 20, HEIGHT // 2 - 20, 40, 40)
item = pg.Rect(400, 300, 30, 30)
speed = 5
score = 0
font = pg.font.Font(None, 36)

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player.x += speed
    if keys[pg.K_LEFT]:
        player.x -= speed
    if keys[pg.K_DOWN]:
        player.y += speed
    if keys[pg.K_UP]:
        player.y -= speed

    player.clamp_ip(screen.get_rect())

    if player.colliderect(item):
        score += 1
        item.topleft = (
            random.randint(0, WIDTH - item.width),
            random.randint(0, HEIGHT - item.height),
        )

    screen.fill(background_color)
    pg.draw.rect(screen, (240, 220, 90), player)
    pg.draw.ellipse(screen, (200, 60, 60), item)
    score_surf = font.render(f"Punkte: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

    pg.display.flip()
    clock.tick(60)

pg.quit()
