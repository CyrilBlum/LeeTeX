import random
from turtle import *

# Screen()


def waehle_zufaelliges_wort():
    # wähle ein zufälliges Wort aus der Datei helvetismen_ascii.txt aus
    datei = open("helvetismen_ascii.txt")
    woerter = datei.readlines()
    datei.close()
    wort = random.choice(woerter)
    wort.upper()
    wort = wort[:-1]
    return wort


def wort_anzeigen(wort, geratene_buchstaben):
    # zeige die bereits geratenen Buchstaben an und die noch nicht erratenen durch Unterstriche
    # der Aufruf print(wort_anzeigen("HANGMAN", "HGA")) printet z.B. HA_G_A_
    angezeigtes_wort = ""
    for buchstabe in wort:
        if buchstabe in geratene_buchstaben:
            angezeigtes_wort += buchstabe
        else:
            angezeigtes_wort += "_"
    return angezeigtes_wort


def galgen_ascii(station):
    ascii = [
        """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
        """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
    ]
    print(ascii[station])


def galgen_turtle(station):
    radius = 8
    torso = 35
    arm = 0.85 * torso
    bein = 1.05 * torso

    if station == 0:
        hideturtle()
        pensize(3)
        forward(100)
        back(50)
        left(90)
        forward(160)
        left(90)
        forward(50)
        left(90)
        forward(20)
    if station == 1:
        penup()
        forward(2 * radius)
        left(90)
        pendown()
        circle(radius)
        """
        right(90)
        for _ in range(540):
            forward(0.15)
            left(1)
        """
    if station == 2:
        right(90)
        forward(torso)
    if station == 3:
        back(torso)
        right(25)
        forward(arm)
    if station == 4:
        back(arm)
        left(50)
        forward(arm)
    if station == 5:
        back(arm)
        right(25)
        forward(torso)
        right(25)
        forward(bein)
    if station == 6:
        back(bein)
        left(50)
        forward(bein)


def hangman_spielen(wort):
    # starte das Spiel
    print("Lass uns Hangman spielen!")
    erraten = False
    falsche = 0
    geratene_buchstaben = ""
    print("Aktuell gefundene Buchstaben:", wort_anzeigen(wort, geratene_buchstaben))
    galgen_turtle(falsche)

    while (not erraten) and (falsche < 6):
        buchstabe = input("Bitte gib einen Buchstaben ein:\n").upper()
        if buchstabe in geratene_buchstaben:
            print("Den Buchstaben", buchstabe, "hast du schon ausprobiert.")
        elif buchstabe not in wort:
            print(buchstabe, "ist nicht im Wort enthalten.")
            falsche += 1
            geratene_buchstaben += buchstabe
            galgen_turtle(falsche)
        else:
            print("Gut gemacht,", buchstabe, "ist im Wort enthalten.")
            geratene_buchstaben += buchstabe

            # das angezeigte Wort hat keine Lücken "_" mehr => das Wort wurde erraten
            if "_" not in wort_anzeigen(wort, geratene_buchstaben):
                erraten = True

        print(wort_anzeigen(wort, geratene_buchstaben))

    if erraten:
        print("Toll, du hast das Wort erraten!")
    else:
        print(
            "Sorry, du hast alle deine Leben aufgebraucht. Das gesuchte Wort war:", wort
        )


wort = waehle_zufaelliges_wort()
hangman_spielen(wort)
