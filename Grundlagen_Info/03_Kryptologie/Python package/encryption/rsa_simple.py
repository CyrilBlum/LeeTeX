# Primzahlen
p = 3
q = 11
# Berechnung n und phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)
print("n:", n)
print("phi(n):", phi_n)
# Wahl von e (muss teilerfremd zu phi(n) sein)
e = 3  # 3 ist teilerfremd zu phi(n)
# Berechnung von d
d = pow(e, -1, phi_n)
# Öffentlicher und privater Schlüssel
public_key = (e, n)
private_key = (d, n)
print("Öffentlicher Schlüssel:", public_key)
print("Privater Schlüssel:", private_key)
# Nachricht verschlüsseln
m = 12  # Beispielnachricht (muss kleiner als n sein)
c = pow(m, e, n)
print("Verschlüsselte Nachricht:", c)
# Nachricht entschlüsseln
decrypted_m = pow(c, d, n)
print("Entschlüsselte Nachricht:", decrypted_m)
