def ist_schaltjahr(jahr):
    return (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)
