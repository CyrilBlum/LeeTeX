class Zeitschrift(Buch):
    def __init__(self, titel, verlag, isbn, ausgabe):
        super().__init__(titel, verlag, isbn)
        self.ausgabe = ausgabe
    
    def info(self):
        basis_info = super().info()
        return f"{basis_info}, Ausgabe: {self.ausgabe}"

# Beispielnutzung
zeitschrift1 = Zeitschrift("National Geographic", "National Geographic Society", "NGM202405", "Mai 2024")
zeitschrift2 = Zeitschrift("Der Spiegel", "Spiegel-Verlag", "SP202422", "22/2024")

bibliothek.buch_hinzufuegen(zeitschrift1)
bibliothek.buch_hinzufuegen(zeitschrift2)

mitglied1.buch_ausleihen(zeitschrift1)

print("\nZeitschriften in der Bibliothek:")
for buch in bibliothek.buecher:
    if isinstance(buch, Zeitschrift):
        print(buch.info())