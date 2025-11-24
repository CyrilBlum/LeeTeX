def koffer(gewicht):
    if gewicht > 100:
        print("Der Koffer ist zu schwer")
    elif gewicht > 20:
        print(
            "Ihr Koffer hat "
            + str(gewicht - 20)
            + " kg Übergewicht. Das kostet "
            + str(5 * (gewicht - 20))
            + " Franken."
        )
    elif gewicht > 0:
        print("Der Koffer ist gratis")
    else:
        print("Das eingegebene Gewicht ist nicht zulässig!")


koffer(12)
koffer(22)
koffer(105)
koffer(-30)
