def finde_perfekte_zahlen(grenze):
    """Findet und druckt alle perfekten Zahlen bis zur gegebenen Grenze."""
    zahl = 1
    for _ in range(grenze):
        teiler_summe = 0

        teiler = 1
        for _ in range(zahl-1):
            if zahl % teiler == 0:
                teiler_summe += teiler
            teiler += 1

        if zahl == teiler_summe:
            print(f"Perfekte Zahl gefunden: {zahl}")
        
        zahl += 1

finde_perfekte_zahlen(100000)