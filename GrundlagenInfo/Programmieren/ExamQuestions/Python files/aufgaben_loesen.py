zeit_aufgaben = [13, 18, 11, 5]
ausgeschlafen = True
genau_gelesen=[True, True, True, False]
zeit = 0
i=0
repeat len(zeit_aufgaben):
    zeit_aufgabe=zeit_aufgaben[i]
    if not ausgeschlafen:
        zeit_aufgabe*=2
        
    if not genau_gelesen[i]:
        zeit_aufgabe*=2
    
    zeit+=zeit_aufgabe
    i+=1
    

print(zeit)
