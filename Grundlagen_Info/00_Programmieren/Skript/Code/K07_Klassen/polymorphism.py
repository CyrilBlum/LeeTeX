class Tier:
    def geraeusch(self):
        return "Ein Tier macht ein Geräusch"


class Hund(Tier):
    def geraeusch(self):
        return "Wuff"


class Katze(Tier):
    def geraeusch(self):
        return "Miau"


tiere = [Tier(), Hund(), Katze()]
for tier in tiere:
    print(tier.geraeusch())

# Ausgabe:
# Ein Tier macht ein Geräusch
# Wuff
# Miau
