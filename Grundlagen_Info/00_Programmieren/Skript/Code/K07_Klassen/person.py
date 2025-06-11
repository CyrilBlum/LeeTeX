class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def geburtstag_feiern(self):
        self.alter += 1
        print(f"{self.name} ist jetzt {self.alter} Jahre alt.")
    
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name} und {self.alter} Jahre alt.")

# Objekte der Klasse Person erstellen
anna = Person("Anna", 16)
jan = Person("Jan", 17)

# Methoden aufrufen
anna.vorstellen()  # Ausgabe: Hallo, ich bin Anna und 16 Jahre alt.
jan.vorstellen()   # Ausgabe: Hallo, ich bin Jan und 17 Jahre alt.

# Geburtstag feiern
anna.geburtstag_feiern()  # Ausgabe: Anna ist jetzt 17 Jahre alt.