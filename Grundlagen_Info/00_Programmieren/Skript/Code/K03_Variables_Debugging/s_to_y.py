sekunden_gesamt = 123456789

# Umrechnungsfaktoren
SEK_PRO_MINUTE = 60
SEK_PRO_STUNDE = 60 * SEK_PRO_MINUTE
SEK_PRO_TAG = 24 * SEK_PRO_STUNDE
SEK_PRO_JAHR = 365 * SEK_PRO_TAG

# Jahre berechnen und den Rest behalten
jahre = sekunden_gesamt // SEK_PRO_JAHR
rest = sekunden_gesamt % SEK_PRO_JAHR

# Tage aus dem verbleibenden Rest berechnen
tage = rest // SEK_PRO_TAG
rest = rest % SEK_PRO_TAG

# Stunden aus dem verbleibenden Rest
stunden = rest // SEK_PRO_STUNDE
rest = rest % SEK_PRO_STUNDE

# Minuten und die uebrig bleibenden Sekunden
minuten = rest // SEK_PRO_MINUTE
sekunden = rest % SEK_PRO_MINUTE

print(f"{sekunden_gesamt} Sekunden sind {jahre} Jahre, {tage} Tage, {stunden} Stunden, {minuten} Minuten und {sekunden} Sekunden.")