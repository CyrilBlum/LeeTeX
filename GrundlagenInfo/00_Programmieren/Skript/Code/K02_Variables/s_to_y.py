y = 60 * 60 * 24 * 365 # Sekunden pro Jahr
d = y / 365 # Sekunden pro Tag
h = d / 24  # Sekunden pro Stunde
m = h / 60 # Sekunden pro Minute
s = m / 60 # Sekunden pro Sekunde

y_ganz = 123456789 // y
d_ganz = int(123456789 % y // d)
h_ganz = int(123456789 % y % d // h)
m_ganz = int(123456789 % y % d % h // m)
s_ganz = int(123456789 % y % d % h % m / s)

print("123456789 Sekunden sind " + str(y_ganz) + " Jahre, " + str(d_ganz) + " Tage, " + str(h_ganz) + " Stunden, " + str(m_ganz) + " Minuten und " + str(s_ganz) + " Sekunden.")