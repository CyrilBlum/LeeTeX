y = 60*60*24*365
d = y/365
h = d/24
m = h/60
s = m/60
print("123456789 Sekunden sind "+ str(123456789//y)+" Jahre, " + str(int(123456789%y // d)) + 
" Tage, "+ str(int(123456789%y%d//h)) + " Stunden, " + str(int(123456789%y%d%h//m)) + " Minuten und " + str(int(123456789%y%d%h%m/s)) + 
' Sekunden.')