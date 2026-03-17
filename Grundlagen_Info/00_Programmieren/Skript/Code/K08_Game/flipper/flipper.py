import math as m
import pygame as pg
import random as r

HEIGHT = 1000
WIDTH = int(HEIGHT/800 * 500)
WINDOW = (WIDTH, HEIGHT)
FPS = 60
SPEEDUP = FPS/60

# --- Initialisierung ---
pg.init()
pg.mixer.init()

screen = pg.display.set_mode(WINDOW, pg.SCALED)
pg.display.set_caption("flipper")
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

pg.mixer.init()

# --- Sounds ---
flipper_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/pinball13.mp3")
stick_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/pinball27.mp3")
stick_release_sound = pg.mixer.Sound("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/pinball34.mp3")

# --- Bilder ---
dollar = pg.image.load("Grundlagen_Info/00_Programmieren/Skript/Code/K09_Game/assets/euro.png").convert_alpha()
dollar = pg.transform.scale(dollar, (60, 60))

class StickObj:
    def __init__(self, position, width, height, color):
        self.rect = pg.Rect(position[0], position[1], width, height)
        self.color = color
        self.sticky_duration = 0
        self.direction_stick_x = 0
        self.direction_stick_y = 0
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.rect.center, self.rect.width // 2)

    def was_hit(self):
        if self.sticky_duration == 0:
            self.direction_stick_x = r.choice((-1,1))
            self.direction_stick_y = r.choice((-1,1))
            stick_sound.play()
            self.sticky_duration = 120  # frames

    def update(self, ball, score, step_ballx, step_bally):
        if self.sticky_duration > 1:
            self.sticky_duration -= 1
            if self.sticky_duration % 15 == 0:
                self.color = (r.randint(100,255), r.randint(100,255), r.randint(100,255))
            step_bally = 0
            step_ballx = 0
            
        elif self.sticky_duration == 1:
            score += 5
            stick_release_sound.play()
            
            ball.centerx = self.rect.centerx + self.direction_stick_x*30
            ball.centery = self.rect.centery + self.direction_stick_y*30
            step_ballx = self.direction_stick_x * 5
            step_bally = self.direction_stick_y * 5
            self.sticky_duration -= 1

        return ball, score, step_ballx, step_bally
        

    

class CollectObj:
    """
    Objekt auf dem Flipperkasten, welches eingesammelt werden kann.
    """
    def __init__(self, position, radius, color):
        self.rect = pg.Rect(position[0], position[1], radius*2, radius*2)
        self.position = position
        self.radius = radius
        self.color = color
        self.collected = False
    
    def draw(self, screen):
        if not self.collected:
            screen.blit(dollar, (self.position[0], self.position[1]))
            


class Flipper:
    """    Klasse für einen Flipper im Flipperspiel.
    Der Flipper kann sich drehen, um den Ball abzuwehren.
    Attributes:
        start_base (tuple): (x, y) Koordinaten des Flipper-Start
        length (int): Länge des Flippers
        start_angle (float): Startwinkel des Flippers in Grad
        max_up_angle (float): Maximaler Winkel, den der Flipper nach oben schlagen
            kann in Grad
        speed (float): Geschwindigkeit, mit der der Flipper sich bewegt in Grad pro Frame
        width (int): Breite des Flippers
        color (tuple): Farbe des Flippers
    Methods:
        update_angle(is_pressed): Aktualisiert den Winkel des Flippers basierend darauf,
            ob die Taste gedrückt ist.
        calculate_flipper_end_base(): Berechnet die Endposition des Flippers basierend
            auf dem aktuellen Winkel.
        update(): Aktualisiert die Endposition und den aktuellen Winkel des Flippers
            basierend auf dem aktuellen Winkel.
        get_y_at_x(x, top=True): Berechnet für die y-Koordinate am Flipper für eine gegebene
            x-Koordinate (z.B. Ballposition).
        get_y_perc_at_x(x): Berechnet die relative Position entlang des Flippers für eine gegebene
            x-Koordinate (z.B. Ballposition).
        draw(screen): Zeichnet den Flipper auf den Bildschirm.
        get_speed_at_x(x): Berechnet die aktuelle Geschwindigkeit des Flippers an einer gegebenen
            x-Koordinate.
        collides_with_ball(ball): Überprüft, ob der Ball mit dem Flipper kollidiert, also ob der Ball die Fläche
            des Flippers berührt.
    """

    def __init__(
        self, start_base, length, start_angle, max_up_angle, speed, width, color, bounceback_factor=1, flipper_type="left"
    ):
        """
        :param start_base: (x, y) Koordinaten des Flipper-Startpunkts
        :param length: Länge des Flippers
        :param start_angle: Startwinkel des Flippers in Grad
        :param max_up_angle: Maximaler Winkel, den der Flipper nach oben schlagen kann in Grad
        :param speed: Geschwindigkeit, mit der der Flipper sich bewegt in Grad pro Frame
        :param width: Breite des Flippers
        :param color: Farbe des Flippers
        """
        self.start_base = start_base
        self.length = length
        self.start_angle = start_angle
        self.START_ANGLE = start_angle
        self.current_angle = self.START_ANGLE
        self.end_base = self.calculate_flipper_end_base()
        self.max_up_angle = max_up_angle
        self.speed = speed
        self.width = width
        self.current_speed = 0
        self.color = color
        self.flipper_type = flipper_type    
        self.max_angle = start_angle + max_up_angle
        self.bounceback_factor = bounceback_factor
        

    def update_angle(self, is_pressed):
        """
        Aktualisiert den Winkel des Flippers basierend darauf, ob die Taste gedrückt ist.

        :param is_pressed: Bool, ob die Taste gedrückt ist
        """
        if is_pressed:
            # Flipper schlägt nach oben, bis zum Maximalwinkel
            if self.flipper_type == "left":
                self.current_angle = min(self.max_angle, self.current_angle + self.speed)
                if self.current_speed == 0 and self.current_angle < self.max_angle:
                    flipper_sound.play()
                # if moving up, speed is set to self.speed
                if self.current_angle < self.max_angle:
                    self.current_speed = self.speed
                # if not moving, speed is 0
                else:
                    self.current_speed = 0
            else:  # right flipper
                self.current_angle = max(self.max_angle, self.current_angle - self.speed)
                # if moving up, speed is set to self.speed
                if self.current_speed == 0 and self.current_angle > self.max_angle:
                    flipper_sound.play()
                if self.current_angle > self.max_angle:
                    self.current_speed = self.speed
                # if not moving, speed is 0
                else:
                    self.current_speed = 0
            

        else:
            # Flipper fällt zurück Richtung 0°
            if self.flipper_type == "left":
                self.current_angle = max(self.START_ANGLE, self.current_angle - self.speed)
                # if moving down, speed is set to -self.speed
                if self.current_angle > self.START_ANGLE:
                    self.current_speed = -self.speed
                # if not moving, speed is 0
                else:
                    self.current_speed = 0
            else:  # right flipper
                self.current_angle = min(self.START_ANGLE, self.current_angle + self.speed)
                # if moving down, speed is set to -self.speed
                if self.current_angle < self.START_ANGLE:
                    self.current_speed = -self.speed
                # if not moving, speed is 0
                else:
                    self.current_speed = 0
            

    def calculate_flipper_end_base(self):
        end_x = self.start_base[0] + self.length * m.cos(m.radians(self.current_angle))
        end_y = self.start_base[1] - self.length * m.sin(m.radians(self.current_angle))
        return (end_x, end_y)

    def update(self):
        """
        Aktualisiert die Endposition und den aktuellen Winkel des Flippers basierend auf dem aktuellen Winkel.
        """
        self.end_base = self.calculate_flipper_end_base()

    def get_y_at_x(self, x, top=True):
        """
        Berechnet für die y-Koordinate am Flipper für eine gegebene x-Koordinate (z.B. Ballposition).
        :param x: x-Koordinate
        """
        min_x = min(self.start_base[0], self.end_base[0])
        max_x = max(self.start_base[0], self.end_base[0])

        if x < min_x or x > max_x:
            return None

        t = self.get_y_perc_at_x(
            x
        )  # berechne, wie weit auf der Flipperlänge wir sind (0 bis 1)
        dy = (
            self.end_base[1] - self.start_base[1]
        )  # Änderung in y-Richtung entlang des gesamten Flippers
        y = self.start_base[1] + dy * t + (-self.width // 2 if top else self.width // 2)
        return y

    def get_y_perc_at_x(self, x):
        """
        Berechnet die relative Position entlang des Flippers für eine gegebene x-Koordinate (z.B. Ballposition).
        :param x: x-Koordinate
        :return: relative Position (0 bis 1) entlang des Flippers
        """
        flipper_length = self.end_base[0] - self.start_base[0]
        position = (x - self.start_base[0]) / flipper_length
        return position

    def draw(self, screen):
        """
        Zeichnet den Flipper auf den Bildschirm.
        :param screen: Pygame Bildschirm
        """
        pg.draw.line(screen, self.color, self.start_base, self.end_base, self.width)

    def get_speed_at_x(self, x):
        """
        Berechnet die aktuelle Geschwindigkeit des Flippers an einer gegebenen x-Koordinate.
        :param x: x-Koordinate
        :return: Geschwindigkeit des Flippers an dieser Position
        """
        perc = self.get_y_perc_at_x(x)
        if self.flipper_type == "left":
            return self.current_speed * perc
        else:  # right flipper
            return self.current_speed * (1 - perc)

    def collides_with_ball(self, ball):
        """
        Überprüft, ob der Ball mit dem Flipper kollidiert, also ob der Ball die Fläche des Flippers berührt.
        Funktioniert auch, wenn der ball bereits unterhalb des Flippers ist.
        :param ball: Pygame Rect des Balls
        :return: Bool, ob eine Kollision stattfindet
        """
        y_flipper_top = self.get_y_at_x(ball.centerx, top=True)
        y_flipper_bottom = self.get_y_at_x(ball.centerx, top=False)

        if y_flipper_top is None or y_flipper_bottom is None:
            return False

        return ball.bottom >= y_flipper_top and ball.top <= HEIGHT
