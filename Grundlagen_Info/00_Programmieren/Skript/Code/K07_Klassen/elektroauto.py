# Elternklasse
class Fahrzeug:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.km_stand = 0

    def fahren(self, strecke):
        self.km_stand += strecke
        print(f"Fahre {strecke} km. Neuer Kilometerstand: {self.km_stand} km")

    def info(self):
        return f"{self.marke} {self.modell} ({self.baujahr}), {self.km_stand} km"

# Kindklasse
class ElektroAuto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, batterie_kapazitaet):
        super().__init__(marke, modell, baujahr)  # Elternklassen-Konstruktor aufrufen
        self.batterie_kapazitaet = batterie_kapazitaet
        self.ladezustand = 100  # Prozent

    def laden(self):
        self.ladezustand = 100
        print(f"{self.marke} {self.modell} wurde vollständig geladen.")

    def fahren(self, strecke):
        verbrauch = strecke * 0.2  # 20% Verbrauch pro 100 km
        if self.ladezustand - verbrauch >= 0:
            self.km_stand += strecke
            self.ladezustand -= verbrauch
            print(
                f"Fahre {strecke} km elektrisch. Ladezustand: {self.ladezustand:.1f}%")
        else:
            print("Nicht genug Batterieladung für diese Strecke!")

    def info(self):
        basis_info = super().info()  # Methode der Elternklasse aufrufen
        return f"{basis_info}, Batterie: {self.batterie_kapazitaet} kWh, Ladung: {self.ladezustand:.1f}%"


# Objekte erstellen
normales_auto = Fahrzeug("VW", "Golf", 2020)
elektro_auto = ElektroAuto("Tesla", "Model 3", 2021, 75)

# Methoden testen
normales_auto.fahren(100)
print(normales_auto.info())

elektro_auto.fahren(200)
print(elektro_auto.info())
elektro_auto.laden()
print(elektro_auto.info())