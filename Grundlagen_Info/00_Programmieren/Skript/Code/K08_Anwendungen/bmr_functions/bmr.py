def harris_benedict(gewicht, groesse, alter, geschlecht):
    if geschlecht == 'mann':
        return 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    elif geschlecht == 'frau':
        return 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)

def mifflin_st_jeor(gewicht, groesse, alter, geschlecht):
    if geschlecht == 'mann':
        return (10 * gewicht) + (6.25 * groesse) - (5 * alter) + 5
    elif geschlecht == 'frau':
        return (10 * gewicht) + (6.25 * groesse) - (5 * alter) - 161

def katch_mcardle(gewicht, koerperfettanteil):
    fettfreie_masse = gewicht * (1 - koerperfettanteil)
    return 370 + (21.6 * fettfreie_masse)

def durchschnitt_bmr(gewicht, groesse, alter, geschlecht, koerperfettanteil):
    bmr_harris = harris_benedict(gewicht, groesse, alter, geschlecht)
    bmr_mifflin = mifflin_st_jeor(gewicht, groesse, alter, geschlecht)
    bmr_katch = katch_mcardle(gewicht, koerperfettanteil)
    
    durchschnitt = (bmr_harris + bmr_mifflin + bmr_katch) / 3
    return durchschnitt

# Beispiel
durchschnitt = durchschnitt_bmr(75, 180, 30, "mann", .12)
print(f"Der durchschnittliche Grundumsatz beträgt {durchschnitt:.2f} Kilokalorien")