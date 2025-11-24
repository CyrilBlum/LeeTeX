hauptstaedte = {
    "Schweiz": "Hier gibt es keine Hauptstadt, nur eine Bundesstadt.",
    "Deutschland": "Berlin",
    "Frankreich": "Paris",
}
land = input("Land eingeben: ")
if land in hauptstaedte:
    print("Die Hauptstadt ist:", hauptstaedte[land])
else:
    print("Land nicht gefunden.")
