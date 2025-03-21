def schaltjahr(jahr):
    if (jahr-2024)%4 == 0:
        print("Schaltjahr!")
    else:
        print("Kein Schaltjahr!")

schaltjahr(2029)