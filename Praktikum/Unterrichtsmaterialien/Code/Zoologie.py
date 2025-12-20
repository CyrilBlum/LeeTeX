class Lebewesen:
    gesamt_population = 0

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        Lebewesen.gesamt_population += 1

    def zeige_basisdaten(self):
        print(f"Lebewesen Name: {self.name} Alter: {self.alter}")

    @classmethod
    def get_gesamt_population(cls):
        return cls.gesamt_population

pilz = Lebewesen("Pilz", 1)
baum = Lebewesen("Baum", 10)
pilz.zeige_basisdaten()
print(f"Gesamtpopulation erwartet: 2, tatsächlich: {Lebewesen.get_gesamt_population()}")
