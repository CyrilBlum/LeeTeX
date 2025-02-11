# Dies ist ein Zeilenkommentar.
# Ein Zeilenkommentar beginnt mit einem Rautesymbol / Hashtag.
print("Treffende Kommentare können dem Verständnis dienlich sein.")

"""
Dies ist ein Blockkommentar.
Ein solcher Kommentar darf sich über mehrere Zeilen erstrecken.

Ein Blockkommentar beginnt und endet mit jeweils drei Anführungszeichen.

Kommentare werden von Python ignoriert.
Diese Eigenschaft kann man sich zu
Nutze machen, um ausgewählte Programmteile temporär zu deaktivieren.
"""

# Wäre die folgende Zeile nicht kommentiert, würden wir
# einen Fehler erhalten (Divsion durch Null):
# print(7 / 0)

# Diese Berechnung ist aber ok:
print(7 / 3)

# Kommentare beginnen erst NACH dem Rautesymbol:
print("Das WIRD geprintet.")  # das wird aber ignoriert
