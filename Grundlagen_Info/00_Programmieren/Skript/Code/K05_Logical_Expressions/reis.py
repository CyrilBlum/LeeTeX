def reis(n):
	summe = 0
	pro_feld = 1
	count = 0
	while count < n:
		summe += pro_feld
		pro_feld *= 2
		count += 1
	return(summe)

reisk = reis(64)
print(reisk)