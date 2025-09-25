class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def geburtstag_feiern(self):
        self.alter += 1
        print(f"{self.name} ist jetzt {self.alter} Jahre alt.")
    
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name} und {self.alter} Jahre alt.")

class Schueler(Person):
    def __init__(self, name, alter, klasse):
        super().__init__(name, alter)
        self.klasse = klasse
    
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}, {self.alter} Jahre alt und besuche die Klasse {self.klasse}.")
    
    def klasse_wechseln(self, neue_klasse):
        self.klasse = neue_klasse
        print(f"{self.name} besucht jetzt die Klasse {self.klasse}.")

# Test
person = Person("Anna", 35)
schueler = Schueler("Max", 16, "4b")

person.vorstellen()
person.geburtstag_feiern()

schueler.vorstellen()
schueler.geburtstag_feiern()
schueler.klasse_wechseln("5a")
schueler.vorstellen()