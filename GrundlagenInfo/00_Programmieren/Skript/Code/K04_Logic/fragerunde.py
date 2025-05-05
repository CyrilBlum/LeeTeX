richtige_antworten = 0

frage1 = input("Wie viele Planeten hat unser Sonnensystem? ")
if frage1 == "8":
    richtige_antworten += 1

frage2 = input("Welches ist das größte Land der Welt?")
if frage2 == "Russland":
    richtige_antworten += 1

frage3 = input("In welchem Jahr war die erste Mondlandung?")
if frage3 == "1969":
    richtige_antworten += 1

# Ergebnis ausgeben
print("Du hast " + str(richtige_antworten) + " von 3 Fragen richtig beantwortet!")
