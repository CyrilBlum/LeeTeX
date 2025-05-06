def bmi_rueckmeldung(bmi, geschlecht):
    if geschlecht == "m":
        if bmi < 16:
            return "Starkes Untergewicht"
        elif bmi < 17.5:
            return "Mässiges Untergewicht"
        elif bmi < 20:
            return "Leichtes Untergewicht"
        elif bmi < 25:
            return "Normalgewicht"
        elif bmi < 30:
            return "Leichtes Übergewicht"
        else:
            return "Starkes Übergewicht"
    elif geschlecht == "w":
        if bmi < 16:
            return "Starkes Untergewicht"
        elif bmi < 17.5:
            return "Mässiges Untergewicht"
        elif bmi < 19:
            return "Leichtes Untergewicht"
        elif bmi < 24:
            return "Normalgewicht"
        elif bmi < 30:
            return "Leichtes Übergewicht"
        else:
            return "Starkes Übergewicht"
    else:
        return "Ungültiges Geschlecht"

print(bmi_rueckmeldung(22.5, "w"))