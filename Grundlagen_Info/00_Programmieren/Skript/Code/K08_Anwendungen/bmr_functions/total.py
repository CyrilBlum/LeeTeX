from leistungsumsatz import *
from bmr import *

l_zeit = [60, 20]  # Zeit in Minuten
l_kcal = [16.5, 6]  # Kilokalorien pro Minute

gewicht = 75  # in Kg
groesse = 180  # in cm
alter = 30  # in Jahren
geschlecht = "mann"
koerperfettanteil = 0.12  # in %

bmr = durchschnitt_bmr(gewicht, groesse, alter, geschlecht, koerperfettanteil)
l = berechne_leistungsumsatz(l_zeit, l_kcal)


def berechne_total(bmr, l):
    return bmr + l


total = berechne_total(bmr, l)
print(total)
