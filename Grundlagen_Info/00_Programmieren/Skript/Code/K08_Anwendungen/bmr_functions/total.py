from leistungsumsatz import *
from bmr import *

l_zeit = [60, 20]  # Zeit in Minuten
l_kcal = [16.5, 6]  # Kalorien pro Minute
gewicht = 75  # kg
groesse = 180  # cm
alter = 30  # jahre
geschlecht = 'mann'
koerperfettanteil = 0.12  # 12%

print("TESTE", l_zeit)

bmr = durchschnitt_bmr(gewicht, groesse, alter, geschlecht, koerperfettanteil)
l = berechne_leistungsumsatz(l_zeit, l_kcal)


def berechne_total(bmr, l):
    return bmr + l

total = berechne_total(bmr, l)
print(total)