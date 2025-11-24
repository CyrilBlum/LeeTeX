class Bankkonto:
    def __init__(self, kontonummer, inhaber, kontostand):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"CHF {betrag} eingezahlt. Neuer Kontostand: CHF {self.kontostand}")
        else:
            print("Fehler: Betrag muss positiv sein")

    def abheben(self, betrag):
        if betrag > 0:
            if betrag <= self.kontostand:
                self.kontostand -= betrag
                print(
                    f"CHF {betrag} abgehoben. Neuer Kontostand: CHF {self.kontostand}"
                )
            else:
                print("Fehler: Nicht genügend Guthaben")
        else:
            print("Fehler: Betrag muss positiv sein")

    def kontoinfo(self):
        print(f"Konto {self.kontonummer} ({self.inhaber}): CHF {self.kontostand}")


# Objekt erstellen
mein_konto = Bankkonto("CH123456", "Lea Müller", 1000)

# Methoden aufrufen
mein_konto.kontoinfo()
mein_konto.einzahlen(500)
mein_konto.abheben(200)
mein_konto.kontoinfo()
