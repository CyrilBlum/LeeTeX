sekunden_gesamt = 123456789

# Umrechnungsfaktoren
SEK_PRO_MINUTE = 60
SEK_PRO_STUNDE = 3600
SEK_PRO_TAG = 86400
SEK_PRO_JAHR = 31536000

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