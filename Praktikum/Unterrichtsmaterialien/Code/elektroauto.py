class Tier:
    def __init__(self, name):
        self.name = name

    def atmen(self):
        return f"{self.name} atmet."

class Katze(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)
        self.rasse = rasse

    def miau(self):
        return f"{self.name}, die {self.rasse}, miaut."

karlchen = Katze(name="Karlchen", rasse="Siamkatze")
print(karlchen.atmen()) # Zugriff auf die geerbte Methode 'atmen'
print(karlchen.miau()) # Zugriff auf die eigene Methode 'miau'
