class Produkt:
    anzahl_produkte = 0  # Klassenattribut für alle Produkte

    def __init__(self, name, preis):
        self.name = name
        self.preis = preis
        Produkt.anzahl_produkte += 1  # Erhöhe bei jeder neuen Instanz

    @classmethod
    def get_anzahl_produkte(cls):
        print("Anzahl Produkte:", cls.anzahl_produkte)


# Objekte erstellen
p_1 = Produkt("Laptop", 1200)
p_2 = Produkt("Smartphone", 800)
p_3 = Produkt("Maus", 30)

Produkt.get_anzahl_produkte()  # Anzahl Produkte: 3
