
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

class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, inhaber, kontostand=0, zinssatz=0.01):
        super().__init__(kontonummer, inhaber, kontostand)
        self.zinssatz = zinssatz
    
    def zinsen_gutschreiben(self):
        zinsen = self.kontostand * self.zinssatz
        self.kontostand += zinsen
        print(f"CHF {zinsen:.2f} Zinsen gutgeschrieben. Neuer Kontostand: CHF {self.kontostand:.2f}")
    
    def kontoinfo(self):
        basis_info = super().kontoinfo()
        return f"{basis_info} (Zinssatz: {self.zinssatz*100:.2f}%)"

# Test
sparkonto = Sparkonto("CH789", "Sarah", 1000, 0.02)
print(sparkonto.kontoinfo())
sparkonto.einzahlen(500)
sparkonto.zinsen_gutschreiben()
print(sparkonto.kontoinfo())