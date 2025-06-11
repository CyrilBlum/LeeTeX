def wetter_kleider(temperatur):
    if temperatur > 100: 
        print("Ungültige Zahl")
    if temperatur < 100:
        print("Hosen")
        print("T-Shirt")
    if temperatur < 10:
        print("Pulli")
    if temperatur < 0:
        print("Jacke")

wetter_kleider(-5)