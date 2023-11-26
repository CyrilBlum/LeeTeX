# finanzen, taschengeld

taschengeld=50 # monatliches Taschengeld
spar_anteil=0.1 # gesparter Anteil in %
wunsch_objekte=["Kleider", "Lese-Lampe", "Wecker", "Games", "Spielzeug", "Comics"]
wunsch_kosten = [10, 50, 11, 32, 15, 3]
meine_objekte=[]
geld=0

repeat 12:
    geld+=taschengeld*spar_anteil
    kann_kaufen=True
    while kann_kaufen and len(wunsch_objekte)>0:
        kann_kaufen=False
        i=0
        repeat len(wunsch_objekte):
            if wunsch_kosten[i] <= geld:
                meine_objekte.append(wunsch_objekte[i])
                geld-=wunsch_kosten[i]
                wunsch_objekte.remove(wunsch_objekte[i])
                wunsch_kosten.remove(wunsch_kosten[i])
                kann_kaufen=True
                break
            i+=1

print(meine_objekte)
print(geld)
    
    


