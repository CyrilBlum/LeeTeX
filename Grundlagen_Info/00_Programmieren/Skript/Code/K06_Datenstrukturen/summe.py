def summiere(daten):
	i = 0           # Hilfs-Index, um auf Elemente von daten zuzugreifen
	summe = 0       # Variable, um alle Elemente von "daten" zu summieren
	
	# Durch alle Elemente von Daten durchgehen und zu Summe hinzufügen
	for _ in range(len(daten)):
		summe += daten[i]   # Wert von daten[i] zu Summe hinzufügen
		i += 1              # Hilfs-Index um 1 vergrössern (Werte?)
		
	print(summe)
	
summiere([4, 2, -6, 17, 5, 12]) # Ausgabe: 34