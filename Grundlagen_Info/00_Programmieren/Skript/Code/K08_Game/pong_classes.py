import pygame
import sys
import random

# Pygame initialisieren
pygame.init()

# Bildschirm-Einstellungen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Spiel")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spiel-Einstellungen
FPS = 60
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10
PADDLE_SPEED = 6
BALL_SPEED = 5

# Schläger-Klasse
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
       
    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
           
        # Begrenzung auf Bildschirm
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
   
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball-Klasse
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = BALL_SPEED * random.choice((1, -1))
   
    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
       
        # Kollision mit oberen/unteren Wänden
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy
   
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
   
    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = BALL_SPEED * random.choice((1, -1))

# Spiel-Initialisierung
def init_game():
    # Schläger erstellen
    paddle1 = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)  # Links
    paddle2 = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)  # Rechts
   
    # Ball erstellen
    ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)
   
    # Punktzahlen
    score1 = 0
    score2 = 0
   
    return paddle1, paddle2, ball, score1, score2

# Haupt-Spiel-Funktion
def main():
    # Spiel initialisieren
    paddle1, paddle2, ball, score1, score2 = init_game()
   
    # Clock für FPS
    clock = pygame.time.Clock()
   
    # Schrift für Punktzahlen
    font = pygame.font.Font(None, 74)
   
    # Spiel-Loop
    running = True
    while running:
        # Events verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        # Tasten-Input
        keys = pygame.key.get_pressed()
       
        # Spieler 1 Steuerung (W/S)
        if keys[pygame.K_w]:
            paddle1.move(up=True)
        if keys[pygame.K_s]:
            paddle1.move(up=False)
       
        # Spieler 2 Steuerung (Pfeiltasten)
        if keys[pygame.K_UP]:
            paddle2.move(up=True)
        if keys[pygame.K_DOWN]:
            paddle2.move(up=False)
       
        # Spiel beenden
        if keys[pygame.K_ESCAPE]:
            running = False
       
        # Ball bewegen
        ball.move()
       
        # Kollision mit Schlägern
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx = -ball.dx
       
        # Punktzahl aktualisieren
        if ball.rect.left <= 0:
            score2 += 1
            ball.reset()
        elif ball.rect.right >= WIDTH:
            score1 += 1
            ball.reset()
       
        # Bildschirm zeichnen
        screen.fill(BLACK)
       
        # Mittellinie zeichnen
        for y in range(0, HEIGHT, 20):
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 1, y, 2, 10))
       
        # Spiel-Objekte zeichnen
        paddle1.draw()
        paddle2.draw()
        ball.draw()
       
        # Punktzahlen zeichnen
        score_text1 = font.render(str(score1), True, WHITE)
        score_text2 = font.render(str(score2), True, WHITE)
        screen.blit(score_text1, (WIDTH // 4, 20))
        screen.blit(score_text2, (3 * WIDTH // 4, 20))
       
        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
   
    # Pygame beenden
    pygame.quit()
    sys.exit()

# Spiel starten
if __name__ == "__main__":
    main()