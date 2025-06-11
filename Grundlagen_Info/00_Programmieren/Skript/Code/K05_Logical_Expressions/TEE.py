bmr = durchschnitt_bmr(gewicht, groesse, alter, geschlecht, koerperfettanteil)
l = berechne_leistungsumsatz(l_zeit, l_kcal)

def berechne_total(bmr, l):
    return bmr + l

total = berechne_total(bmr, l)