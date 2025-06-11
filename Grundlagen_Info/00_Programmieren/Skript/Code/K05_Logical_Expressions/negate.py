# Aufgabe 1: Ist die Person nicht volljährig?
def temperatur_ist_angenehm(temperatur):
    if temperatur >= 20 and temperatur <= 25:
        print("Die Temperatur ist angenehm.")
    else:
        print("Die Temperatur ist nicht angenehm.")




# Aufgabe
def ist_nicht_volljaehrig(alter):
    """
    Überprüft, ob eine Person nicht volljährig ist.
    :param alter: Alter der Person (int)
    """
    # Schüler-Code:
    if alter >= 18:
        print(False)
    else:
        print(True)

# Lösung:
def ist_nicht_volljaehrig_loesung(alter):
    """
    Überprüft, ob eine Person nicht volljährig ist.
    :param alter: Alter der Person (int)
    """
    ist_volljaehrig = alter >= 18
    nicht_volljaehrig = not ist_volljaehrig
    print(nicht_volljaehrig)

# Aufgabe 2: Ist die Temperatur nicht angenehm? (zwischen 20 und 25 Grad)
def ist_temperatur_nicht_angenehm(temperatur):
    """
    Überprüft, ob die Temperatur nicht angenehm ist.
    :param temperatur: Temperatur in Grad Celsius (int)
    """
    # Schüler-Code:
    pass

# Lösung:
def ist_temperatur_nicht_angenehm_loesung(temperatur):
    """
    Überprüft, ob die Temperatur nicht angenehm ist.
    :param temperatur: Temperatur in Grad Celsius (int)
    """
    ist_angenehm = 20 <= temperatur <= 25
    nicht_angenehm = not ist_angenehm
    print(nicht_angenehm)

# Aufgabe 3: Ist die Zahl weder positiv noch gerade?
def ist_weder_positiv_noch_gerade(zahl):
    """
    Überprüft, ob die Zahl weder positiv noch gerade ist.
    :param zahl: Eine ganze Zahl (int)
    """
    # Schüler-Code:
    pass

# Lösung:
def ist_weder_positiv_noch_gerade_loesung(zahl):
    """
    Überprüft, ob die Zahl weder positiv noch gerade ist.
    :param zahl: Eine ganze Zahl (int)
    """
    ist_positiv = zahl > 0
    ist_gerade = zahl % 2 == 0
    weder_positiv_noch_gerade = not (ist_positiv or ist_gerade)
    print(weder_positiv_noch_gerade)

# Aufgabe 4: Sind beide Aussagen falsch? (z.B. "Es regnet" und "Es ist kalt")
def sind_beide_aussagen_falsch(aussage1, aussage2):
    """
    Überprüft, ob beide Aussagen falsch sind.
    :param aussage1: Erste Aussage (bool)
    :param aussage2: Zweite Aussage (bool)
    """
    # Schüler-Code:
    pass

# Lösung:
def sind_beide_aussagen_falsch_loesung(aussage1, aussage2):
    """
    Überprüft, ob beide Aussagen falsch sind.
    :param aussage1: Erste Aussage (bool)
    :param aussage2: Zweite Aussage (bool)
    """
    beide_wahr = aussage1 or aussage2
    beide_falsch = not beide_wahr
    print(beide_falsch)

# Aufgabe 5: Ist die Zahl nicht im Bereich von 10 bis 50 (inklusive)?
def ist_zahl_nicht_im_bereich(zahl):
    """
    Überprüft, ob die Zahl nicht im Bereich von 10 bis 50 ist.
    :param zahl: Eine ganze Zahl (int)
    """
    # Schüler-Code:
    pass

# Lösung:
def ist_zahl_nicht_im_bereich_loesung(zahl):
    """
    Überprüft, ob die Zahl nicht im Bereich von 10 bis 50 ist.
    :param zahl: Eine ganze Zahl (int)
    """
    im_bereich = 10 <= zahl <= 50
    nicht_im_bereich = not im_bereich
    print(nicht_im_bereich)

# Beispielaufrufe für die Lösungen:
# ist_nicht_volljaehrig_loesung(16)  # True
# ist_nicht_volljaehrig_loesung(18)  # False
# ist_temperatur_nicht_angenehm_loesung(15)  # True
# ist_temperatur_nicht_angenehm_loesung(22)  # False
# ist_weder_positiv_noch_gerade_loesung(-3)  # True
# ist_weder_positiv_noch_gerade_loesung(4)   # False
# sind_beide_aussagen_falsch_loesung(False, False)  # True
# sind_beide_aussagen_falsch_loesung(True, False)   # False
# ist_zahl_nicht_im_bereich_loesung(5)  # True
# ist_zahl_nicht_im_bereich_loesung(30) # False
