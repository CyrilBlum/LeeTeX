import numpy as np

def erlaubt(zeile, spalte, ziffer, gitter):
	n = int(np.sqrt(len(gitter[0])))

	for j in range(n**2):
		if gitter[zeile][j] == ziffer:
			return False

	for i in range(n**2):
		if gitter[i][spalte] == ziffer:
			return False

	zeile_block = zeile - (zeile % n)
	spalte_block = spalte - (spalte % n)
	for i_block in range(n):
		for j_block in range(n):
			if gitter[zeile_block+i_block][spalte_block+j_block] == ziffer:
				return False
	return True

def sudoku(gitter):
	# Gehe durch alle Felder im Gitter.
	for zeile in range(9):
		for spalte in range(9):
			# Schaue, ob das Feld noch leer ist.
			if gitter[zeile][spalte] == 0:
				# leeres Feld gefunden

				# Gehen durch alle 10 Ziffern 1 bis 9.
				for ziffer in range(1,10):
					# Prüfe, ob die Ziffer für diese Feld erlaubt ist.
					if erlaubt(zeile,spalte,ziffer,gitter):
						# Die betrachtete Ziffer ist erlaubt.

						# Schreibe diese Ziffer in das Feld.
						gitter[zeile][spalte] = ziffer

						# Die Ziffer wurde ins Gitter geschrieben.
						# Arbeite nun rekrusiv mit dem neuen Gitter weiter.
						sudoku(gitter)

						gitter[zeile][spalte] = 0
						
						# leeres Feld für welches keine Ziffer passt
						# => Sackgasse gefunden => Backtracking
				return
	# gültige Lösung gefunden
	print(np.array(gitter))
	return

gitter_start1 = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

sudoku(gitter_start1)