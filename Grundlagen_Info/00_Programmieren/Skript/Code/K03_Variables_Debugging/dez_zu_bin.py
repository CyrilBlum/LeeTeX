"""
Dieses Programm wandelt Dezimalzahlen in Binärzahlen um
Die eingegebene Dezimalzahl muss kleiner als 1024 sein.
"""

# die folgende Dezimalzahl soll umgewandelt werden
zahl = int(input("Welche Zahl soll umgewandelt werden? "))

# Beginnen mit der groessten Basisgroesse
# für 16 Bit Zahlen ist dies 65535
basisgroesse = 2**15

binaerzahl = ""

# Berechnung der 10 Ziffern der Binärzahl
for _ in range(16):
    # Ziffer: Wie häufig passt die Basisgrösse in den Betrag?
    ziffer = zahl // basisgroesse

    # die Ziffer wird in einen String umgewandelt und an die Binärzahl angehängt
    binaerzahl += str(ziffer)

    #  Welche Zahl muss durch die weiteren Basisgrössen abgedeckt werden?
    zahl -= ziffer * basisgroesse

    # Basisgrösse wird auf die nächst kleinere Basisgrösse gesetzt.
    basisgroesse //= 2

# Ausgabe der Binärzahl
print(f"Die binäre Darstellung der eingegebenen Zahl ist: {binaerzahl}")
