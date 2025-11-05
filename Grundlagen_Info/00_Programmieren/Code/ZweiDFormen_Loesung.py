import math

class ZweiDForm:
    def __init__(self, name, dimensionen=2):
        self.name = name
        self.dimensionen = dimensionen

    def berechne_flaeche(self):
        print(f"ACHTUNG: Die Methode 'berechne_flaeche' muss in der Unterklasse {self.name} definiert werden.")
        return 0

    def berechne_umfang(self):
        print(f"ACHTUNG: Die Methode 'berechne_umfang' muss in der Unterklasse {self.name} definiert werden.")
        return 0

class Kreis(ZweiDForm):
    def __init__(self, radius):
        super().__init__("Kreis")
        self.radius = radius

    def berechne_flaeche(self):
        return math.pi * self.radius**2

    def berechne_umfang(self):
        return 2 * math.pi * self.radius

class Rechteck(ZweiDForm):
    def __init__(self, breite, hoehe):
        super().__init__("Rechteck")
        self.breite = breite
        self.hoehe = hoehe

    def berechne_flaeche(self):
        return self.breite * self.hoehe

    def berechne_umfang(self):
        return 2 * (self.breite + self.hoehe)

class RegelmaessigesNEck(ZweiDForm):
    def __init__(self, seitenlaenge, anzahl_ecken):
        super().__init__(f"Regelmäßiges {anzahl_ecken}-Eck")
        self.a = seitenlaenge
        self.n = anzahl_ecken

    def berechne_flaeche(self):
        winkel_rad = math.radians(180 / self.n)
        return (self.n * self.a**2) / (4 * math.tan(winkel_rad))

    def berechne_umfang(self):
        return self.n * self.a

formen_a = [
    Kreis(radius=5),
    Rechteck(breite=4, hoehe=6),
    RegelmaessigesNEck(seitenlaenge=3, anzahl_ecken=6)
]

for form in formen_a:
    print(f"\n--- {form.name} ---")
    print(f"  Fläche: {form.berechne_flaeche():.2f}")
    print(f"  Umfang: {form.berechne_umfang():.2f}")