import math

class GeometrischerKoerper:
    def __init__(self, name, dimensionen):
        self.name = name
        self.dimensionen = dimensionen

    def info(self):
        return f"Objekt: {self.name}, Dimensionen: {self.dimensionen}"

class ZweiDForm(GeometrischerKoerper):
    def __init__(self, name, dimensionen=2):
        super().__init__(name, dimensionen)
        
    def berechne_flaeche(self):
        print(f"ACHTUNG: Die Methode 'berechne_flaeche' muss in der Unterklasse {self.name} definiert werden.")
        return 0

class DreiDForm(GeometrischerKoerper):
    def __init__(self, name):
        super().__init__(name, dimensionen=3)

    def berechne_oberflaeche(self):
        print(f"ACHTUNG: Die Methode 'berechne_oberflaeche' muss in der Unterklasse {self.name} definiert werden.")
        return 0

    def berechne_volumen(self):
        print(f"ACHTUNG: Die Methode 'berechne_volumen' muss in der Unterklasse {self.name} definiert werden.")
        return 0

class Rechteck(ZweiDForm):
    def __init__(self, breite, hoehe):
        super().__init__("Rechteck")
        self.breite = breite
        self.hoehe = hoehe

    def berechne_flaeche(self):
        return self.breite * self.hoehe

class Quadrat(Rechteck):
    def __init__(self, seitenlaenge):
        super().__init__(seitenlaenge, seitenlaenge)
        self.name = "Quadrat"

class RegelmaessigesNEck(ZweiDForm):
    def __init__(self, seitenlaenge, anzahl_ecken):
        super().__init__(f"Regelmäßiges {anzahl_ecken}-Eck")
        self.a = seitenlaenge
        self.n = anzahl_ecken

    def berechne_flaeche(self):
        winkel_rad = math.radians(180 / self.n)
        return (self.n * self.a**2) / (4 * math.tan(winkel_rad))


class PlatonischerKoerper(DreiDForm):
    def __init__(self, name, grundflaeche_objekt, anzahl_flaechen):
        super().__init__(name)
        self.grundflaeche = grundflaeche_objekt 
        self.anzahl_flaechen = anzahl_flaechen

    def berechne_oberflaeche(self):
        flaeche_einer_seite = self.grundflaeche.berechne_flaeche()
        return self.anzahl_flaechen * flaeche_einer_seite
    
    def berechne_volumen(self):
         print(f"ACHTUNG: Volumenberechnung für {self.name} ist komplex und muss in der Unterklasse definiert werden.")
         return 0

# --- Definition der Grundflächen ---
dreieck_seite = RegelmaessigesNEck(seitenlaenge=4, anzahl_ecken=3)
quadrat_seite = Quadrat(seitenlaenge=5)
fuenfeck_seite = RegelmaessigesNEck(seitenlaenge=3, anzahl_ecken=5)

# --- Instanziierung der 5 Platonischen Körper ---
# 1. Tetraeder (4 Dreiecksflächen)
tetraeder = PlatonischerKoerper(
    name="Tetraeder",
    grundflaeche_objekt=dreieck_seite,
    anzahl_flaechen=4
)

# 2. Hexaeder (6 Quadratflächen)
hexaeder = PlatonischerKoerper(
    name="Hexaeder (Würfel)",
    grundflaeche_objekt=quadrat_seite,
    anzahl_flaechen=6
)

# 3. Oktaeder (8 Dreiecksflächen)
oktaeder = PlatonischerKoerper(
    name="Oktaeder",
    grundflaeche_objekt=dreieck_seite,
    anzahl_flaechen=8
)

# 4. Dodekaeder (12 Fünfecksflächen)
dodekaeder = PlatonischerKoerper(
    name="Dodekaeder",
    grundflaeche_objekt=fuenfeck_seite,
    anzahl_flaechen=12
)

# 5. Ikosaeder (20 Dreiecksflächen)
ikosaeder = PlatonischerKoerper(
    name="Ikosaeder",
    grundflaeche_objekt=dreieck_seite,
    anzahl_flaechen=20
)

koerper_c = [tetraeder, hexaeder, oktaeder, dodekaeder, ikosaeder]

print("--- Test C: Alle 5 Platonische Körper ---")
for koerper in koerper_c:
    print(f"\n--- {koerper.name} ---")
    print(f"  Info: {koerper.info()}")
    print(f"  Oberfläche ({koerper.grundflaeche.name} * {koerper.anzahl_flaechen}): {koerper.berechne_oberflaeche():.2f}")
    # Die Volumen-Methode gibt weiterhin nur die Warnung aus
    print(f"  Volumen-Aufruf:")
    koerper.berechne_volumen()