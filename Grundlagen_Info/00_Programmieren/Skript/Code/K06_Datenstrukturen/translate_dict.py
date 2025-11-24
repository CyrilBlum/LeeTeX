deutsch_zu_englisch = {
    "Die": "The",
    "Der": "The",
    "Das": "The",
    "Stuhl": "chair",
    "Sofa": "couch",
    "Lampe": "lamp",
    "ist": "is",
    "rot": "red",
    "blau": "blue",
    "grün": "green",
    "gelb": "yellow",
    "schwarz": "black",
}


def uebersetzen(satz):
    uebersetzter_satz = []
    for wort in satz:
        uebersetzter_satz.append(deutsch_zu_englisch[wort])
    print(uebersetzter_satz)
