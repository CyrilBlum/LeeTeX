l_kcal = [229, 26]
l_gram = [230, 33]

def berechne_kcal_tot(l_kcal, l_gram):
	kcal_total = 0
	index = 0
	for i in range(len(l_kcal)):
		# jedes Element beider Listen miteinander multiplizieren
		# und durch 100 Gramm rechnen
		kcal_total += l_kcal[index] * l_gram[index] / 100
		index += 1
	return kcal_total

kcal = berechne_kcal_tot(l_kcal, l_gram)
print(kcal)