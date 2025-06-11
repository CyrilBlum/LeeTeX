class Bankkonto:
    def __init__(self, kontonummer, inhaber, kontostand=0):
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
                print(f"CHF {betrag} abgehoben. Neuer Kontostand: CHF {self.kontostand}")
                return True
            else:
                print("Fehler: Nicht genügend Guthaben")
                return False
        else:
            print("Fehler: Betrag muss positiv sein")
            return False
    
    def kontoinfo(self):
        return f"Konto {self.kontonummer} ({self.inhaber}): CHF {self.kontostand}"
    
    def ueberweisen(self, zielkonto, betrag):
        if self.abheben(betrag):
            zielkonto.einzahlen(betrag)
            print(f"Überweisung von CHF {betrag} an {zielkonto.inhaber} erfolgreich")

# Test
konto1 = Bankkonto("CH123", "Anna", 1000)
konto2 = Bankkonto("CH456", "Ben", 500)

print(konto1.kontoinfo())
print(konto2.kontoinfo())
konto1.ueberweisen(konto2, 300)
print(konto1.kontoinfo())
print(konto2.kontoinfo())