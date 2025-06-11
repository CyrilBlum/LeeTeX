frage1 = "Wie viele Kegel gibt es beim Bowling?\n"
antwort1 = "9"
frage2 = "Wie nennt man das Kraftwerk einer Zelle?\n"
antwort2 = "Mitochondrium"
frage3 = "Wann endet heute die Schule?\n"
antwort3 = "16:00"

richtige = 0

user_antwort1 = input(frage1)
user_antwort2 = input(frage2)
user_antwort3 = input(frage3)


if user_antwort1 == antwort1:
    richtige += 1

if user_antwort2 == antwort2:
    richtige += 1

if user_antwort3 == antwort3:
    richtige += 1

print(richtige)