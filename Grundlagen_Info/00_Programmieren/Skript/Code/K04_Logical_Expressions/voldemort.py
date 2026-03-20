result = ""
while True:
    word = input("Bitte ein Wort eingeben (oder 'Voldemort', um zu beenden): ")
    if word == "Voldemort":
        break
    if result:
        result += " "
    result += word

print("Eingegebene Wörter:", result)
