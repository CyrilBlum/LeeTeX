def verdreifache_bis_ueber1Mio(zahl):
    anzahl = 0
    while zahl < 1000000:
        zahl *= 3
        print(zahl)
        anzahl += 1
    print("Anzahl Verdreifachungen: ", anzahl)


verdreifache_bis_ueber1Mio(100)
