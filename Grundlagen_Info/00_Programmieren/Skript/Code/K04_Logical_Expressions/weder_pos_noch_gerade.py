# Lösung:
def weder_pos_noch_gerade_not(zahl):
    return not ((zahl > 0) or (zahl % 2 == 0))


# Lösung:
def weder_pos_noch_gerade(zahl):
    return zahl <= 0 and zahl % 2 != 0


print(weder_pos_noch_gerade(3))  # sollte False ausgeben
print(weder_pos_noch_gerade(-3))  # sollte True ausgeben
print(weder_pos_noch_gerade(4))  # sollte False ausgeben
print(weder_pos_noch_gerade(-4))  # sollte False ausgeben
