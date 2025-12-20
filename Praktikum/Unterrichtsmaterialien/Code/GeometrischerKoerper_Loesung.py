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

    def berechne_umfang(self):
        print(f"ACHTUNG: Die Methode 'berechne_umfang' muss in der Unterklasse {self.name} definiert werden.")
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

class Wuerfel(DreiDForm):
    def __init__(self, kantenlaenge):
        super().__init__("Würfel")
        self.a = kantenlaenge

    def berechne_oberflaeche(self):
        return 6 * self.a**2

    def berechne_volumen(self):
        return self.a**3

class Kugel(DreiDForm):
    def __init__(self, radius):
        super().__init__("Kugel")
        self.r = radius

    def berechne_oberflaeche(self):
        return 4 * math.pi * self.r**2

    def berechne_volumen(self):
        return (4/3) * math.pi * self.r**3

koerper_b = [
    Wuerfel(kantenlaenge=5),
    Kugel(radius=3)
]

for koerper in koerper_b:
    print(f"\n--- {koerper.name} ---")
    print(f"  Info: {koerper.info()}") 
    print(f"  Oberfläche: {koerper.berechne_oberflaeche():.2f}")
    print(f"  Volumen: {koerper.berechne_volumen():.2f}")