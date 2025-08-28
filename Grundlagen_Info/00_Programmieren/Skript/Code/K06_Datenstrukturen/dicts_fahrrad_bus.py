wettervorhersage = {
    "Montag": {"Temperatur": 18, "Regen": False},
    "Dienstag": {"Temperatur": 21, "Regen": True},
    "Mittwoch": {"Temperatur": 17, "Regen": False}
}

tag = input("Geben Sie einen Tag ein (z.B. Montag): ")

if tag in wettervorhersage:
    daten = wettervorhersage[tag]
    print(f"Temperatur: {daten['Temperatur']}°C")
    print(f"Regnet es? {'Ja' if daten['Regen'] else 'Nein'}")
    if daten['Regen'] or daten['Temperatur'] < 15:
        print("Ich gehe mit dem Bus")
    else:
        print("Ich gehe per Fahrrad")
else:
    print("Tag nicht gefunden.")