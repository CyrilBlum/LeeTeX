geschlecht = input("Bitte geben Sie Ihr Geschlecht ein (m/w): ")
alter = int(input("Bitte geben Sie Ihr Alter ein: "))

if alter < 17:
    print("Sie sind noch nicht AHV-pflichtig.")
elif (alter < 64) or ((alter < 65) and geschlecht == "m"):
    print("Sie sind AHV-pflichtig.")
else:
    print("Sie empfangen bereits AHV.")
