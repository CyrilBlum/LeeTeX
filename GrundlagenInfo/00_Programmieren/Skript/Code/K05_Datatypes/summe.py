def summiere(daten):
	i = 0           # Hilfs-Index, um auf Elemente von daten zuzugreifen
	summe = 0       # Variable, um alle Elemente von "daten" zu summieren
	n = len(daten)  # Anzahl Elemente in "daten" (Wert?)
	
	# Durch alle Elemente von Daten durchgehen und zu Summe hinzufügen
	for _ in range(n):
		summe += daten[i]   # Wert von daten[i] zu Summe hinzufügen
		i += 1              # Hilfs-Index um 1 vergrössern (Werte?)
		
	print(summe)
	
summiere([4, 2, -6, 17, 5, 12])