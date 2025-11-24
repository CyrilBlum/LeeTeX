from tank import *
from terrain import *
from datetime import datetime

# from settings import *

font = pg.font.Font(None, 24)
clock = pg.time.Clock()

running = True
winner = None
show_help = False

init_terrain()

# Generate tanks
t1 = Tank(70, (120, 200, 90, 255), 1, W, H)
t2 = Tank(W - 70 - 80, (200, 90, 90, 255), -1, W, H)

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        elif e.type == pg.KEYDOWN:
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
            f"© Cyril Wendl, {datetime.now().year}",
        ]
        pad = 8
        x = 20
        y = 20
        for line in lines:
            t = font.render(line, True, (240, 240, 240))
            screen.blit(t, (x, y))
            y += t.get_height() + pad
    pg.display.flip()
    clock.tick(60)

pg.quit()
