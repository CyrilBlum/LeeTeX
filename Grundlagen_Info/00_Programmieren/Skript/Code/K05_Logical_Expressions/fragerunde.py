richtige_antworten = 0

frage_1 = int(input("Wie viele Planeten hat unser Sonnensystem?"))
if frage_1 == 8:
    richtige_antworten += 1

frage_2 = input("Welches ist das grösste Land der Welt?")
if frage_2 == "Russland":
    richtige_antworten += 1

frage_3 = int(input("In welchem Jahr war die erste Mondlandung?"))
if frage_3 == 1969:
    richtige_antworten += 1

# Ergebnis ausgeben
print("Du hast " + str(richtige_antworten) + " von 3 Fragen richtig beantwortet!")
