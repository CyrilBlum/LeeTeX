def notenskala(max_punkte, erreichte_punkte):
    return erreichte_punkte / max_punkte * 5 + 1


anzahl_pruef = int(input("Wie viele Prüfungen sind es? "))

pruef_nr = 1
summe_noten = 0
for _ in range(anzahl_pruef):
    max_p = float(input("Maximale Punkte der Prüfung " + str(pruef_nr) + "? "))
    erreicht_p = float(input("Erreichte Punkte an der Prüfung " + str(pruef_nr) + "? "))
    note = notenskala(max_p, erreicht_p)
    print("Note an der " + str(pruef_nr) + "-te Prüfung: "+ str(note))
    summe_noten += note
    pruef_nr += 1

schnitt = summe_noten / anzahl_pruef
print("Schnitt der Noten: ", schnitt)
