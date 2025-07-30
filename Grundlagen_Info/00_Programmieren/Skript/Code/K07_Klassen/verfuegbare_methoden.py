# Zeige verfügbare Methoden für eingebaute Typen mit dir()

# Für eine konkrete Instanz
x = [1, 2, 3]
print("Methoden für die Instanz x (Liste):")
print(dir(x))

# Für den Klassennamen selbst
print("Methoden für die Klasse 'list':")
print(dir(list)) # gibt dasselbe Ergebnis wie dir(x) aus

# Beispiel für einen anderen Typ (str)
s = "hallo"
print("Methoden für die Instanz s (String):")
print(dir(s))

print("Methoden für die Klasse 'str':")
print(dir(str)) # gibt dasselbe Ergebnis wie dir(s) aus
