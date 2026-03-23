import math


def flaeche_dreieck(h, b):
    return b * h / 2


total_flaeche = 0
h = 1
dreieck_nr = 1
for _ in range(16):
    b = math.sqrt(dreieck_nr)
    total_flaeche += flaeche_dreieck(h, b)
    dreieck_nr += 1

print("Die Fläche der Spirale beträgt", total_flaeche)
