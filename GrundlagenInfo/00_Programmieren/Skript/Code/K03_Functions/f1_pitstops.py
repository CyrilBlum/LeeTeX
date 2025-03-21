def fahrzeit_ohne_stopps(strecke_km, geschwindigkeit_kmh):
    """Berechnet die reine Fahrzeit in Sekunden"""
    zeit_stunden = strecke_km / geschwindigkeit_kmh
    zeit_sekunden = zeit_stunden * 3600
    return zeit_sekunden

def gesamtzeit_mit_stopps(strecke_km, geschwindigkeit_kmh, anzahl_stopps, stoppdauer_sek):
    """Berechnet die Gesamtzeit inklusive Stopps"""
    fahrzeit_sek = fahrzeit_ohne_stopps(strecke_km, geschwindigkeit_kmh)
    gesamtzeit_sek = fahrzeit_sek + (anzahl_stopps * stoppdauer_sek)
    return gesamtzeit_sek

# Beispielwerte
strecke = 305
v = 210
stoppdauer = 25

# Strategie 1: 1 Stopp
zeit = gesamtzeit_mit_stopps(strecke, v, 1, stoppdauer)

print("Gesamtzeit mit Stopps: " + str(zeit))