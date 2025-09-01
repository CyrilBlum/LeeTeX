schueler_a = ["Mathe", "Englisch", "Informatik", "Biologie"]
schueler_b = ["Mathe", "Englisch", "Kunst", "Musik"]
schueler_c = ["Informatik", "Englisch", "Sport", "Geschichte"]

pflichtkurse = ["Mathe", "Englisch"]
wahlkurse   = ["Informatik", "Biologie", "Kunst", "Musik", "Sport", "Geschichte"]

# Mengen
set_a = set(schueler_a)
set_b = set(schueler_b)
set_c = set(schueler_c)

set_pflicht = set(pflichtkurse)
set_wahl = set(wahlkurse)

# 1. Alle belegten Kurse
alle_kurse = set_a | set_b | set_c

# 2. Gemeinsame Kurse aller drei Schüler
gemeinsam_alle = set_a & set_b & set_c

# 3. Exklusive Kurse von Schüler A
exklusiv_a = set_a - (set_b | set_c)

# 4. Pflichtkurse, die jemand NICHT gewählt hat
nicht_bei_allen = set_pflicht - (set_a & set_b & set_c)

# 5. Wahlkurse, die alle drei gewählt haben
wahl_gemeinsam = set_wahl & set_a & set_b & set_c

# Ausgabe
print("Alle belegten Kurse:", alle_kurse)
print("Gemeinsame Kurse aller:", gemeinsam_alle)
print("Exklusiv nur Schüler A:", exklusiv_a)
print("Pflichtkurse, die fehlen:", nicht_bei_allen)
print("Gemeinsame Wahlkurse:", wahl_gemeinsam)