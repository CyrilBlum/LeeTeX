class Buch:
    def __init__(self, titel, autor, seitenzahl):
        self.titel = titel
        self.autor = autor
        self.seitenzahl = seitenzahl
    
    def info(self):
        print(f'{self.titel}: Buch von {self.autor}, {self.seitenzahl} Seiten')

# Zwei Buchobjekte erstellen
buch_1 = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 335)
buch_2 = Buch("Die unendliche Geschichte", "Michael Ende", 420)

# Methode aufrufen
buch_1.info()
buch_2.info()