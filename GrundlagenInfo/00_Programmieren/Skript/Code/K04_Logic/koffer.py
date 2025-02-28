def koffer(gewicht):
    # überprüft, ob "gewicht" eine Zahl ist
    if not isinstance(gewicht, (int, float)):
        print("Das eingegebene Gewicht ist nicht zulässig!")
    elif gewicht > 100:
        print("Der Koffer ist zu schwer")
    elif gewicht > 20:
        print("Ihr Koffer hat", gewicht-20, "kg Übergewicht. Das kostet",5*(gewicht-20),"Franken.")
    elif gewicht > 0:
        print("Der Koffer ist gratis")
    else:
        print("Das eingegebene Gewicht ist nicht zulässig!")

koffer(12)