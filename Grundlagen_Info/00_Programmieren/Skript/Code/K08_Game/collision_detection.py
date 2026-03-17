import pygame

# 1. Initialisierung
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kollisions-Beispiel")
clock = pygame.time.Clock()

# --- KLASSEN ---

class Spieler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Erstellt die Grafik für den Spieler
        self.image = pygame.Surface((50, 50))
        self.image.fill("cyan")
        # Das 'rect' ist der wichtigste Teil für Kollisionen (die Hitbox)
        self.rect = self.image.get_rect()

    def update(self):
        # Der Spieler folgt der Mausposition
        self.rect.center = pygame.mouse.get_pos()

class Muenze(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill("gold")
        self.rect = self.image.get_rect(topleft=(x, y))

# --- SETUP ---

# Erstelle den Spieler und packe ihn in eine Gruppe (GroupSingle für einzelne Objekte)
spieler = Spieler()
spieler_gruppe = pygame.sprite.GroupSingle(spieler)

# Erstelle eine Gruppe für alle Münzen
muenz_gruppe = pygame.sprite.Group()
for i in range(8):
    neue_muenze = Muenze(i * 100 + 50, 200)
    muenz_gruppe.add(neue_muenze)

# --- HAUPTSCHLEIFE ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logik aktualisieren
    spieler_gruppe.update()

    # KOLLISIONS-CHECK:
    # spritecollide(objekt, gruppe, dokill)
    # Wenn 'dokill' auf True steht, wird die Münze bei Berührung automatisch gelöscht.
    treffer_liste = pygame.sprite.spritecollide(spieler, muenz_gruppe, True)

    if treffer_liste:
        print(f"{len(treffer_liste)} Münze(n) eingesammelt!")

    # Zeichnen
    screen.fill("#202020") # Dunkelgrauer Hintergrund
    
    # Gruppen haben eine eingebaute draw-Funktion
    muenz_gruppe.draw(screen)
    spieler_gruppe.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) # Begrenzung auf 60 Bilder pro Sekunde

pygame.quit()