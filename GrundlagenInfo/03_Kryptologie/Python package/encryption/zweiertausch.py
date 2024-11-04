 def zweiertausch(klartext):
     geheimtext = "" # leerer String
     b = 0
     while b < (len(klartext) - 1):
         geheimtext += klartext[b + 1] + klartext[b]
         b += 2
 
     if len(klartext) % 2 != 0:
         # Klartexte ungerader Länge
         geheimtext += klartext[len(klartext) - 1]
    print(geheimtext)
 
# Verwendung: 
# zweiertausch("KANTONSSCHULE")