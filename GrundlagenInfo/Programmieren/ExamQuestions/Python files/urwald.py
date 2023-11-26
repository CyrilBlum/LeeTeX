baeume_kosten=[2,10,39,230]
baeume_anzahl=[21042, 334, 23345, 1140]
i = 0 # Index für die beiden obigen Listen
gesamtkosten=0 # kosten, um alle Bäume im Urwald zu retten
geld=1000000 # Gesamtes Geld, das investiert werden kann
gesamtflaeche=0 # Gesamte Urwaldfläche
flaeche_gerettet=0 # Fläche, die gerettet wird
geld_aufgebraucht=False 

repeat len(baeume_kosten):
    kosten_i=baeume_kosten[i] # kosten für einen Baum der Art i
    anzahl_i=baeume_anzahl[i] # Anzahl Bäume der Art i
    
    gesamtflaeche += 5*anzahl_i # Fläche, die durch ALLE Bäume der ART i besetzt ist
    gesamtkosten += anzahl_i*kosten_i # Kosten, um ALLE Bäume der ART i zu retten
    
    # berechne, 
    anzahl_baeume_art_gerettet=0
    
    repeat:
        if anzahl_baeume_art_gerettet == anzahl_i:
            break
        if geld < kosten_i:
            break
        flaeche_gerettet+=5
        geld -= kosten_i
        anzahl_baeume_art_gerettet += 1
        if geld < kosten_i:
            geld_aufgebraucht=True
        
    i+=1

print(gesamtflaeche)
print(flaeche_gerettet)
print(flaeche_gerettet/gesamtflaeche*100)
print(gesamtkosten)    
