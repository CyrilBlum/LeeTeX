import numpy as np

def erlaubt(zeile, spalte, ziffer, gitter):
  # prüfe, ob 'ziffer' bereits in der gegeben Zeile vorkommt
  # (fixiere die Zeile und gehe durch alle Spalten)
  for j in range(4):
      if gitter[zeile][j] == ziffer:
          return False

  # prüfe, ob 'ziffer' bereits in der gegeben Spalte vorkommt
  # (fixiere die Spalte und gehe durch alle Zeilen)
  for i in range(4):
      if gitter[i][spalte] == ziffer:
          return False

  # berechne Indizes der "linken oberen Ecke" des relevanten 4er-Blocks
  zeile_block = zeile - (zeile % 2)
  spalte_block = spalte - (spalte % 2)
  # prüfe, ob 'ziffer' bereits in dem relevanten 4er-Block vorkommt
  for i_block in range(2):
      for j_block in range(2):
          if gitter[zeile_block+i_block][spalte_block+j_block] == ziffer:
              return False
  return True

gitter0 = [
[0,1,0,0],
[0,0,0,0],
[0,3,0,2],
[0,0,3,0]
]

gitter1 = [
[0,0,4,0],
[0,4,0,1],
[3,0,0,0],
[0,2,0,0]
]

gitter2 = [
[0,0,4,0],
[0,4,0,0],
[3,0,0,0],
[0,2,0,0]
]


def nonzero(x):
    if (int(x) != 0):
        return int(x)
    else:
        return ''

def sudoku_to_tikz(grid):
    for i in range(9):
        print('\\setrow',end = '',sep = '')
        for j in range(9):
            print('{',nonzero(grid[i][j]),'}',end = '',sep = '')
        print('\n')
    print('\n\n')

#sudoku_to_tikz(np.array(gitter_start4))
#sudoku_to_tikz(np.array(gitter_sol3) - np.array(gitter_start3))

#print(erlaubt(4,7,2,gitter_start3))
def erlaubt_allgemein(zeile, spalte, ziffer, gitter):
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

def sudoku_mini(gitter):
  for zeile in range(4):
      for spalte in range(4):
          if gitter[zeile][spalte] == 0:
              for ziffer in range(1,5):
                  if erlaubt_allgemein(zeile,spalte,ziffer,gitter):
                      # wir versuchen es mit der Wahl 'ziffer'
                      # für dieses Feld
                      gitter[zeile][spalte] = ziffer

                      # und arbeiten mit dieser neuen
                      # Situation rekursiv weiter
                      sudoku_mini(gitter)

                      # die gesetzte 'ziffer' war falsch
                      # deshalb entfernen wir sie wieder
                      gitter[zeile][spalte] = 0
              return
  print(np.array(gitter))
  
sudoku_mini(gitter0)

print(len(gitter0[0]))

