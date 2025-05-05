def fahrzeit_ohne_stopps(strecke, kmh):
    """Berechnet die reine Fahrzeit in Sekunden"""
    zeit_stunden = strecke / kmh
    zeit_sekunden = zeit_stunden * 3600
    return zeit_sekunden

def gesamtzeit(strecke, kmh, stopps, stoppdauer):
    """Berechnet die Gesamtzeit inklusive Stopps"""
    fahrzeit_sek = fahrzeit_ohne_stopps(strecke, kmh)
    gesamtzeit_sek = fahrzeit_sek + (stopps * stoppdauer)
    return gesamtzeit_sek

# Beispielwerte
strecke = 305
v = 210
stoppdauer = 25

# Strategie 1: 1 Stopp
zeit = gesamtzeit(strecke, v, 1, stoppdauer)

print("Gesamtzeit mit Stopps: " + str(zeit))