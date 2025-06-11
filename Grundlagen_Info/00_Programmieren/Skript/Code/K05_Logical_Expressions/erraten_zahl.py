import random

def erraten_zahl():
    # Zufallszahl generieren
    ziel_zahl = random.randint(1, 100)
    
    while True:
        # Benutzereingabe
        eingabe = int(input("Rate die Zahl: "))
        
        if eingabe < ziel_zahl:
            print("Die Zahl ist grösser.")
        elif eingabe > ziel_zahl:
            print("Die Zahl ist kleiner.")
        else:
            print("Richtig! Du hast die Zahl erraten.")
            break

# Funktion testen
erraten_zahl()