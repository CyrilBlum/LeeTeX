class Schulklasse:
    maximal_handy_zeit = 15 
    aufsichtsperson = "Rektor" 
    pausenregeln = ["Nicht rennen", "Müll wegräumen"]  

class Klasse5A(Schulklasse):
    maximal_handy_zeit = 10
    pausenregeln = Schulklasse.pausenregeln.copy()

    @classmethod
    def regel_hinzufuegen(cls, regel):
        cls.pausenregeln.append(regel)

print(f"Basis-Handyzeit: {Schulklasse.maximal_handy_zeit}")
print(f"Basis-Regeln: {Schulklasse.pausenregeln}")

schueler_5a = Klasse5A()
print(f"1. Instanz-Handyzeit (Klasse5A): {schueler_5a.maximal_handy_zeit}") 
print(f"2. Schulklasse Handyzeit (Basis): {Schulklasse.maximal_handy_zeit}") 
print(f"3. Instanz-Aufsicht (geerbt): {schueler_5a.aufsichtsperson}")

schueler_5a.regel_hinzufuegen("Keine Handys im Pausenhof")
print(f"1. Instanz Regeln (Klasse5A): {schueler_5a.pausenregeln}")
print(f"2. Schulklasse Regeln (Basis): {Schulklasse.pausenregeln}")
