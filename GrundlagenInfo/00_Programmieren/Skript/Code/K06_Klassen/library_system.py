class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.ausgeliehen = False
    
    def info(self):
        status = "ausgeliehen" if self.ausgeliehen else "verfügbar"
        return f'"{self.titel}" von {self.autor} (ISBN: {self.isbn}) - {status}'

class Bibliotheksmitglied:
    def __init__(self, name, mitgliedsnummer):
        self.name = name
        self.mitgliedsnummer = mitgliedsnummer
        self.ausgeliehene_buecher = []
    
    def buch_ausleihen(self, buch):
        if not buch.ausgeliehen:
            self.ausgeliehene_buecher.append(buch)
            buch.ausgeliehen = True
            print(f"{self.name} hat '{buch.titel}' ausgeliehen.")
            return True
        else:
            print(f"Fehler: '{buch.titel}' ist bereits ausgeliehen.")
            return False
    
    def buch_zurueckgeben(self, buch):
        if buch in self.ausgeliehene_buecher:
            self.ausgeliehene_buecher.remove(buch)
            buch.ausgeliehen = False
            print(f"{self.name} hat '{buch.titel}' zurückgegeben.")
            return True
        else:
            print(f"Fehler: {self.name} hat '{buch.titel}' nicht ausgeliehen.")
            return False
    
    def info(self):
        anzahl = len(self.ausgeliehene_buecher)
        info = f"{self.name} (Nr. {self.mitgliedsnummer}) - {anzahl} Bücher ausgeliehen"
        if anzahl > 0:
            info += ":\n"
            for buch in self.ausgeliehene_buecher:
                info += f"- {buch.titel}\n"
        return info

class Bibliothek:
    def __init__(self, name):
        self.name = name
        self.buecher = []
        self.mitglieder = []
    
    def buch_hinzufuegen(self, buch):
        self.buecher.append(buch)
        print(f"Buch '{buch.titel}' wurde zur Bibliothek hinzugefügt.")
    
    def mitglied_registrieren(self, mitglied):
        self.mitglieder.append(mitglied)
        print(f"{mitglied.name} wurde als Mitglied registriert.")
    
    def buch_suchen(self, suchbegriff):
        ergebnisse = []
        for buch in self.buecher:
            if (suchbegriff.lower() in buch.titel.lower() or 
                suchbegriff.lower() in buch.autor.lower() or 
                suchbegriff in buch.isbn):
                ergebnisse.append(buch)
        return ergebnisse
    
    def verfuegbare_buecher(self):
        return [buch for buch in self.buecher if not buch.ausgeliehen]
    
    def statistik(self):
        verfuegbar = len(self.verfuegbare_buecher())
        ausgeliehen = len(self.buecher) - verfuegbar
        return f"Bibliothek {self.name}:\n" \
               f"- Gesamtzahl Bücher: {len(self.buecher)}\n" \
               f"- Verfügbare Bücher: {verfuegbar}\n" \
               f"- Ausgeliehene Bücher: {ausgeliehen}\n" \
               f"- Anzahl Mitglieder: {len(self.mitglieder)}"

# Beispielverwendung
bibliothek = Bibliothek("Stadtbibliothek Winterthur")

# Bücher erstellen und hinzufügen
buch1 = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", "9783551557414")
buch2 = Buch("Der Herr der Ringe", "J.R.R. Tolkien", "9783608939842")
buch3 = Buch("Die unendliche Geschichte", "Michael Ende", "9783522202664")

bibliothek.buch_hinzufuegen(buch1)
bibliothek.buch_hinzufuegen(buch2)
bibliothek.buch_hinzufuegen(buch3)

# Mitglieder erstellen und registrieren
mitglied1 = Bibliotheksmitglied("Lisa Müller", "M001")
mitglied2 = Bibliotheksmitglied("Tom Schneider", "M002")

bibliothek.mitglied_registrieren(mitglied1)
bibliothek.mitglied_registrieren(mitglied2)

# Bücher ausleihen
mitglied1.buch_ausleihen(buch1)
mitglied2.buch_ausleihen(buch3)

# Suche durchführen
print("\nSuchergebnisse für 'Harry':")
ergebnisse = bibliothek.buch_suchen("Harry")
for buch in ergebnisse:
    print(buch.info())

# Statistik anzeigen
print("\n" + bibliothek.statistik())

# Infos zu Mitgliedern anzeigen
print("\nMitgliederinformationen:")
print(mitglied1.info())
print(mitglied2.info())

# Buch zurückgeben
mitglied1.buch_zurueckgeben(buch1)

# Aktualisierte Statistik
print("\n" + bibliothek.statistik())