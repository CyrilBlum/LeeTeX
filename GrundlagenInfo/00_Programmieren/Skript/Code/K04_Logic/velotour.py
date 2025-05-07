def bewertung_fahrradtour(distanz_km, hoehenmeter):
    if distanz_km < 20:
        print("Zu kurz")
    elif distanz_km <= 60 and hoehenmeter <= 500:
        print("Gute Tour")
    else:
        print("Zu lang")

# Beispielaufrufe
bewertung_fahrradtour(15, 300)  # Erwartet: "Zu kurz"
bewertung_fahrradtour(50, 400)  # Erwartet: "Gute Tour"
bewertung_fahrradtour(70, 600)  # Erwartet: "Zu lang"