class Schueler:
    schule = "Kantonsschule im Lee"  # Klassenattribut
    
    def __init__(self, name, klasse):
        self.name = name  # Instanzattribut
        self.klasse = klasse  # Instanzattribut
    
    def info(self):
        return f"{self.name}, Klasse {self.klasse}, {self.schule}"

# Objekte erstellen
s1 = Schueler("Lisa", "3a")
s2 = Schueler("Tim", "4b")

print(s1.info())  # Lisa, Klasse 3a, Kantonsschule im Lee
print(s2.info())  # Tim, Klasse 4b, Kantonsschule im Lee

# Klassenattribut über die Klasse ändern
Schueler.schule = "KLW"

# Änderung wirkt sich auf alle Instanzen aus
print(s1.info())  # Lisa, Klasse 3a, KLW
print(s2.info())  # Tim, Klasse 4b, KLW