import pygame
import random
import sys

# Initialisierung
pygame.init()

# Fenstergrösse
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paddle Game")

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
PINK = (255, 100, 180)

# Spiel-Objektgrössen
PUCK_RADIUS = 10 * SCREEN_WIDTH / 400
PADDLE_WIDTH = 50 * SCREEN_WIDTH / 400
PADDLE_HEIGHT = 10 * SCREEN_WIDTH / 400
PADDLE_Y = SCREEN_HEIGHT - 30

# Bewegungsgeschwindigkeit
PUCK_SPEED_OPTIONS = [-5, -4, -3, -2, 2, 3, 4, 5]
PADDLE_SPEED = 8

# Schriftarten
font_big = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 30)


# Spielzustände
def reset_game():
    return {
        "puck_x": SCREEN_WIDTH // 2,
        "puck_y": SCREEN_HEIGHT // 2,
        "puck_vx": random.choice(PUCK_SPEED_OPTIONS),
        "puck_vy": random.choice(PUCK_SPEED_OPTIONS),
        "paddle_x": SCREEN_WIDTH // 2,
        "score": 0,
    }


game = reset_game()
running = True
game_active = False
clock = pygame.time.Clock()

# Hauptloop
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start mit Enter
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_active:
                game = reset_game()
                game_active = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game["paddle_x"] -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        game["paddle_x"] += PADDLE_SPEED

    # Paddle im Fenster halten
    game["paddle_x"] = max(
        PADDLE_WIDTH // 2, min(SCREEN_WIDTH - PADDLE_WIDTH // 2, game["paddle_x"])
    )

    if game_active:
        # Ballposition aktualisieren
        game["puck_x"] += game["puck_vx"]
        game["puck_y"] += game["puck_vy"]

        # Kollision mit Wänden
        if (
            game["puck_x"] - PUCK_RADIUS <= 0
            or game["puck_x"] + PUCK_RADIUS >= SCREEN_WIDTH
        ):
            game["puck_vx"] *= -1
        if game["puck_y"] - PUCK_RADIUS <= 0:
            game["puck_vy"] *= -1

        # Kollision mit Paddle
        if (
            PADDLE_Y < game["puck_y"] + PUCK_RADIUS < PADDLE_Y + PADDLE_HEIGHT
            and game["paddle_x"] - PADDLE_WIDTH // 2
            < game["puck_x"]
            < game["paddle_x"] + PADDLE_WIDTH // 2
        ):
            game["puck_vy"] *= -1.05
            game["puck_vx"] *= 1.05
            game["score"] += 1

        # Game Over
        if game["puck_y"] - PUCK_RADIUS > SCREEN_HEIGHT:
            game_active = False

    # Zeichnen
    pygame.draw.circle(
        screen, BLUE, (int(game["puck_x"]), int(game["puck_y"])), PUCK_RADIUS
    )
    paddle_rect = pygame.Rect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_rect.center = (game["paddle_x"], PADDLE_Y)
    pygame.draw.rect(screen, WHITE, paddle_rect)

    if not game_active:
        text = font_small.render("Drücke ENTER um zu starten", True, PINK)
        screen.blit(text, (60, SCREEN_HEIGHT // 2 - 20))
        if game["score"] > 0:
            over_text = font_big.render("Game Over", True, PINK)
            screen.blit(over_text, (80, SCREEN_HEIGHT // 2 - 100))
            score_text = font_small.render("Score: " + str(game["score"]), True, PINK)
            screen.blit(score_text, (150, SCREEN_HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
