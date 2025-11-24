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

    def ueberweisen(self, zielkonto, betrag):
        if betrag <= self.kontostand:
            self.abheben(betrag)
            zielkonto.einzahlen(betrag)
            print(f"Überweisung von CHF {betrag} an {zielkonto.inhaber} erfolgreich")
        else:
            print(f"Fehler: {self.inhaber} hat nicht genügend Guthaben")


# Test
konto_1 = Bankkonto("CH123", "Anna", 1000)
konto_2 = Bankkonto("CH456", "Ben", 500)

konto_1.kontoinfo()
konto_2.kontoinfo()
konto_1.ueberweisen(konto_2, 300)  # Überweisung, sollte klappen
konto_1.ueberweisen(konto_2, 800)  # erneute Überweisung, sollte fehlschlagen
konto_1.kontoinfo()
konto_2.kontoinfo()
