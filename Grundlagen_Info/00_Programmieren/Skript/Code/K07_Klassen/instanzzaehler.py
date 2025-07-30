class Produkt:
    anzahl_produkte = 0  # Klassenattribut für alle Produkte
    
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis
        Produkt.anzahl_produkte += 1  # Erhöhe bei jeder neuen Instanz
    
    @classmethod
    def get_anzahl_produkte(cls):
        return cls.anzahl_produkte

# Objekte erstellen
p1 = Produkt("Laptop", 1200)
p2 = Produkt("Smartphone", 800)
p3 = Produkt("Maus", 30)

print("Anzahl Produkte:", Produkt.get_anzahl_produkte())  # Anzahl Produkte: 3