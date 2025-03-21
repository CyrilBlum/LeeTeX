def durchschnittsgeschwindigkeit(strecke_km, zeit_min):
    zeit_h = zeit_min / 60
    geschwindigkeit = strecke_km / zeit_h
    return geschwindigkeit

# Beispielaufruf
v = durchschnittsgeschwindigkeit(305, 110)  # 305 km in 110 Minuten
print(f"Die Durchschnittsgeschwindigkeit beträgt {v:.2f} km/h.")