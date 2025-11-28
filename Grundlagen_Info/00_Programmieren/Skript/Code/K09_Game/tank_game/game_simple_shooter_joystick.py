from tank import *
from terrain import *
from datetime import datetime
from settings import *

pg.joystick.init()


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pg.font.Font(None, 12)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (255, 255, 255))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = W * 3 / 4
        self.y = 10
        self.line_height = 12

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


# from settings import *

font = pg.font.Font(None, 24)
clock = pg.time.Clock()

running = True
winner = None
show_help = False

init_terrain()

# Get ready to print.
text_print = TextPrint()

# This dict can be left as-is, since pygame will generate a
# pygame.JOYDEVICEADDED event for every joystick connected
# at the start of the program.
joysticks = {}
DEADZONE = 0.3


# ------------------------
# Power-up (Health Kit)
# ------------------------
class PowerUp:
    def __init__(self, x, y, amount=25):
        # Position sits slightly above terrain
        self.x = x
        self.y = y
        self.amount = amount
        self.r = 12  # radius for pickup area and drawing

    def rect(self):
        return pg.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)

    def draw(self, surf):
        # Placeholder drawing: a simple box with "+ Health" text
        # In future, replace with a PNG sprite
        color = (220, 240, 120)
        surf.blit(
            heal_img,
            (self.x - heal_img.get_width() / 2, self.y - heal_img.get_height() / 2),
        )
        label = font.render("Health +", True, (10, 10, 10))
        surf.blit(label, (int(self.x - label.get_width() / 2), int(self.y - 24)))


# Active power-ups and spawn control
powerups = []
next_powerup_time = 180  # frames until next spawn (approx 3s at 60 FPS)
powerup_min = 4 * 60
powerup_max = 8 * 60


def schedule_next_powerup():
    global next_powerup_time
    next_powerup_time = random.randint(powerup_min, powerup_max)


def spawn_powerup():
    # Pick a random X within screen margins
    x = random.randint(30, W - 30)
    # Place just above terrain top at that X
    y = terrain_top_at(x, 24) - 10
    powerups.append(PowerUp(x, y))


# Initialize first spawn schedule
schedule_next_powerup()


def get_tank_for_joystick(instance_id: int):
    # Map joysticks in sorted order to tanks: 0->t1, 1->t2
    try:
        ordered_ids = sorted(joysticks.keys())
        idx = ordered_ids.index(instance_id)
    except ValueError:
        return None
    if idx == 0:
        return t1
    if idx == 1:
        return t2
    return None


# Generate tanks
t1 = Tank(70, (120, 200, 90, 255), 1, W, H)
t2 = Tank(W - 70 - 80, (200, 90, 90, 255), -1, W, H)

while running:
    print(joysticks)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        # Handle hotplugging
        if e.type == pg.JOYDEVICEADDED:
            # This event will be generated when the program starts for every
            # joystick, filling up the list without needing to create them manually.
            joy = pg.joystick.Joystick(e.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_instance_id()} connencted")
        if e.type == pg.JOYDEVICEREMOVED:
            jid = getattr(e, "instance_id", None)
            if jid in joysticks:
                del joysticks[jid]
                print(f"Joystick {jid} disconnected")
        if e.type == pg.JOYBUTTONDOWN:
            jid = getattr(e, "instance_id", getattr(e, "joy", None))
            btn = getattr(e, "button", None)
            tank = get_tank_for_joystick(jid) if jid is not None else None
            if tank is not None:
                if winner is None:
                    if btn == 0:
                        tank.jump()
                    if btn == 1:
                        fire(tank)
                        shoot_sound.play()
                else:
                    if btn in (7, 9):
                        bullets.clear()
                        winner = None
                        init_terrain()
                        # Clear power-ups on restart and reschedule
                        powerups.clear()
                        schedule_next_powerup()
                        for t in [t1, t2]:
                            t.surface.set_alpha(255)
                            t.angle = 0.3
                            t.life = 100
                            t.ground = terrain_top_at(t.x + t.width / 2, t.height)
                            t.y = t.ground
                            t.speed_y = 0
                        t1.x = 70
                        t2.x = W - 70 - 80
                        reload_sound.play()
        if e.type == pg.KEYDOWN:
            if (
                e.key == pg.K_w
                or e.key == pg.K_s
                or e.key == pg.K_UP
                or e.key == pg.K_DOWN
            ):
                moving_sound.play()
            if e.key == pg.K_ESCAPE:
                running = False
            # Toggle help overlay with Ctrl+K
            if (e.key == pg.K_k) and (e.mod & pg.KMOD_CTRL):
                show_help = not show_help
            if winner is None and e.key == pg.K_r:
                print("No winner yet")
            if winner is not None and e.key == pg.K_r:
                print("Restarting game")
                bullets.clear()
                winner = None
                init_terrain()
                powerups.clear()
                schedule_next_powerup()
                for t in [t1, t2]:
                    t.surface.set_alpha(255)
                    t.angle = 0.3
                    t.life = 100
                    # reposition tanks on new terrain
                    t.ground = terrain_top_at(t.x + t.width / 2, t.height)
                    t.y = t.ground
                    t.speed_y = 0
                t1.x = 70
                t2.x = W - 70 - 80

                reload_sound.play()
            if winner is None:
                if e.key == pg.K_SPACE:
                    fire(t1)
                    shoot_sound.play()
                if e.key == pg.K_RETURN:
                    fire(t2)
                    shoot_sound.play()

    keys = pg.key.get_pressed()
    if not winner:
        # Countdown to next power-up spawn
        if next_powerup_time > 0:
            next_powerup_time -= 1
        else:
            spawn_powerup()
            schedule_next_powerup()

        if keys[pg.K_a]:
            t1.move(-speed_tank)
        if keys[pg.K_d]:
            t1.move(speed_tank)
        if keys[pg.K_s]:
            t1.change_angle(-speed_angle)
        if keys[pg.K_w]:
            t1.change_angle(speed_angle)
        if keys[pg.K_q]:
            t1.jump()
        if keys[pg.K_LEFT]:
            t2.move(-speed_tank)
        if keys[pg.K_RIGHT]:
            t2.move(speed_tank)
        if keys[pg.K_DOWN]:
            t2.change_angle(-speed_angle)
        if keys[pg.K_UP]:
            t2.change_angle(speed_angle)
        if keys[pg.K_p]:
            t2.jump()

        # Joystick continuous controls (axes and hats)
        if joysticks:
            ordered = [joysticks[jid] for jid in sorted(joysticks.keys())]
            for idx, joy in enumerate(ordered):
                tank = t1 if idx == 0 else (t2 if idx == 1 else None)
                if tank is None:
                    continue
                # Left stick horizontal for move
                try:
                    ax0 = joy.get_axis(0)
                except Exception:
                    ax0 = 0.0
                if ax0 < -DEADZONE:
                    tank.move(-speed_tank)
                elif ax0 > DEADZONE:
                    tank.move(speed_tank)
                # Left stick vertical for barrel angle (up is negative)
                try:
                    ax1 = joy.get_axis(1)
                except Exception:
                    ax1 = 0.0
                if ax1 < -DEADZONE:
                    tank.change_angle(speed_angle)
                elif ax1 > DEADZONE:
                    tank.change_angle(-speed_angle)
                # D-Pad (hat) as digital fallback
                try:
                    hats_count = joy.get_numhats()
                except Exception:
                    hats_count = 0
                if hats_count > 0:
                    hx, hy = joy.get_hat(0)
                    if hx < 0:
                        tank.move(-speed_tank)
                    elif hx > 0:
                        tank.move(speed_tank)
                    if hy > 0:
                        tank.change_angle(speed_angle)
                    elif hy < 0:
                        tank.change_angle(-speed_angle)

    for b in bullets[:]:
        b.update()
        if b.y >= terrain_top_at(b.x, 1):
            bullets.remove(b)
            continue
        if b.outofscreen():  # bullet out of screen
            bullets.remove(b)
            continue

        if b.owner is t1:
            opponent = t2
        else:
            opponent = t1

        if b.rect().colliderect(opponent.hitbox()):
            if winner is None:
                bullets.remove(b)
                if opponent.life > 0:
                    opponent.has_been_hit(b.x, b.y)

                if min([t1.life, t2.life]) <= 0:
                    print("We have a winner!")
                    if t1.life > t2.life:
                        winner = 0
                    else:
                        winner = 1

    # update tanks (jump physics and clamp to terrain)
    t1.update()
    t2.update()
    screen.fill(BG)
    draw_terrain(screen)
    for t in [t1, t2]:

        t.draw(screen)
        screen.blit(t.surface, (0, 0))
        if t.time_hit > 0:
            t.time_hit -= 1
            ratio = t.time_hit / 60.0
            img = explosion_img.copy()
            img.set_alpha(int(255 * ratio))
            screen.blit(
                img,
                (int(t.hitX - img.get_width() / 2), int(t.hitY - img.get_height() / 2)),
            )

    for b in bullets:
        b.draw(screen)

    # Draw power-ups
    for pu in powerups:
        pu.draw(screen)

    # Power-up pickups (collision with tank hitboxes)
    if winner is None and powerups:
        for t in [t1, t2]:
            for pu in powerups[:]:
                if pu.rect().colliderect(t.hitbox()):
                    heal_sound.play()
                    # Recover life (cap at 100)
                    t.life = min(100, t.life + pu.amount)
                    t.surface.set_alpha(int(t.life / 100 * 255))
                    # Optional pickup feedback: briefly flash
                    # t.time_hit = min(t.time_hit + 20, 60)
                    powerups.remove(pu)

    if winner is not None:
        msg = font.render(f"Tank {winner+1} gewinnt! (R = neu)", True, (255, 220, 120))
        screen.blit(msg, (W // 2 - msg.get_width() // 2, H // 2 - 20))

    if show_help:
        # Draw semi-transparent overlay with controls
        overlay = pg.Surface((W, H), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        lines = [
            "Steuerung (Ctrl+K schliessen)",
            "Spiel verlassen: ESC",
            "Neustart (nach Sieg): R",
            "",
            "Tank 1:",
            "Bewegen: A / D",
            "Rohrwinkel: W / S",
            "Springen: Q",
            "Schiessen: SPACE",
            "",
            "Tank 2:",
            "Bewegen: Pfeil Links / Rechts",
            "Rohrwinkel: Pfeil Hoch / Runter",
            "Springen: P",
            "Schiessen: ENTER",
            "",
            "Controller (Joystick):",
            "Linker Stick: Bewegen/Zielen (hoch/runter)",
            "D-Pad: Bewegen/Zielen (Alternative)",
            "Taste 0 (A): Springen, Taste 1 (B): Schiessen",
            "Start (7/9): Neustart nach Sieg",
            "",
            "Power-Ups:",
            'Gelber Kreis mit "Health +": +25 Leben beim Einsammeln',
            f"© Cyril Wendl, {datetime.now().year}",
        ]
        pad = 8
        x = 20
        y = 20
        for line in lines:
            t = font.render(line, True, (240, 240, 240))
            screen.blit(t, (x, y))
            y += t.get_height() + pad
    # Get count of joysticks.
    joystick_count = pg.joystick.get_count()
    print(f"Number of joysticks: {joystick_count}")
    text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
    text_print.reset()
    text_print.indent()

    # For each joystick:
    for joystick in joysticks.values():
        jid = joystick.get_instance_id()

        text_print.tprint(screen, f"Joystick {jid}")
        text_print.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        text_print.tprint(screen, f"Joystick name: {name}")

        guid = joystick.get_guid()
        text_print.tprint(screen, f"GUID: {guid}")

        power_level = joystick.get_power_level()
        text_print.tprint(screen, f"Joystick's power level: {power_level}")

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other. Triggers count as axes.
        axes = joystick.get_numaxes()
        text_print.tprint(screen, f"Number of axes: {axes}")
        text_print.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
        text_print.unindent()

        buttons = joystick.get_numbuttons()
        text_print.tprint(screen, f"Number of buttons: {buttons}")
        text_print.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            text_print.tprint(screen, f"Button {i:>2} value: {button}")
        text_print.unindent()

        hats = joystick.get_numhats()
        text_print.tprint(screen, f"Number of hats: {hats}")
        text_print.indent()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
        text_print.unindent()

        text_print.unindent()
    pg.display.flip()
    clock.tick(60)

pg.quit()
