
class Auto:
    anzahl_autos = 0

    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        Auto.anzahl_autos += 1
    
    @classmethod
    def get_statisik(cls):
        print(f"Die gesammte Anzahl an Autos is {cls.anzahl_autos}")
    


Audi = Auto("Audi", "A6", 2010)
BMW = Auto("BMW", "i3", 2020)

Auto.get_statisik()