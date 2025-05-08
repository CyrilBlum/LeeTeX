def wetter_kleider(temperatur):
    if temperatur > 100: 
        print("Ungültige Zahl")
    elif temperatur < 100:
        print("Hosen")
        print("T-Shirt")
    elif temperatur < 10:
        print("Pulli")
    elif temperatur < 0:
        print("Jacke")

wetter_kleider(-5)