class Lebewesen:
    gesamt_population = 0

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        Lebewesen.gesamt_population += 1

    def zeige_basisdaten(self):
        print(f"Lebewesen: {self.name}, Alter: {self.alter} Jahre")

    @classmethod
    def get_gesamt_population(cls):
        return cls.gesamt_population

class Tier(Lebewesen):
    def __init__(self, name, alter, art):
        super().__init__(name, alter)
        self.art = art

    def fressen(self):
        print(f"Das Tier {self.name} frisst.")

class Pflanze(Lebewesen):
    def __init__(self, name, alter, farbe):
        super().__init__(name, alter)
        self.farbe = farbe
        self.fotosynthese = True

    def wachsen(self):
        print(f"Die Pflanze {self.name} wächst und benötigt Licht.")

class Saeugetier(Tier):
    anzahl_saeugetiere = 0

    def __init__(self, name, alter, fellfarbe, nahrungsart):
        super().__init__(name, alter, art="Säugetier")
        self.fellfarbe = fellfarbe
        self.nahrungsart = nahrungsart
        Saeugetier.anzahl_saeugetiere += 1

    def fell_pflegen(self):
        print(f"Das Säugetier {self.name} pflegt sein Fell.")

    @classmethod
    def get_anzahl_saeugetiere(cls):
        return cls.anzahl_saeugetiere

pilz = Lebewesen("Pilz", 1)
baum = Lebewesen("Baum", 10)

pilz.zeige_basisdaten()
print(f"Gesamt-Population erwartet: 2, tatsächlich: {Lebewesen.get_gesamt_population()}")

adler = Tier("Adler", 4, "Vogel")

adler.zeige_basisdaten()
adler.fressen()        
print(f"Gesamt-Population erwartet: 3, tatsächlich: {Lebewesen.get_gesamt_population()}")

rose = Pflanze(name="Rose", alter=1, farbe="Rot")

rose.zeige_basisdaten() 
rose.wachsen()          
print(f"Gesamt-Population erwartet: 4, tatsächlich: {Lebewesen.get_gesamt_population()}")

loewe = Saeugetier(name="Löwe", alter=8, fellfarbe="Gelbbraun", nahrungsart="Fleischfresser")
baer = Saeugetier(name="Bär", alter=12, fellfarbe="Braun", nahrungsart="Allesfresser")

loewe.fressen()       
baer.zeige_basisdaten()  
print(f"Gesamt-Population erwartet: 6, tatsächlich: {Lebewesen.get_gesamt_population()}")
print(f"Säugetiere erwartet: 2, tatsächlich: {Saeugetier.get_anzahl_saeugetiere()}")