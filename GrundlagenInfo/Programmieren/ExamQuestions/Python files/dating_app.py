# Unromantische Dating-App
dating_mann = ["James", "Johannes", "Adam", "Ian", "Wilson", "Karl", "Bob", "Chris", "Charles"]
gefaellt_mir = [0.2, 0.3, 0.2, 0.4, 0.7, 0.3, 0.3, 0.2, 0.7]
gefaellt_ihm = [0.5, 0.2, 0.4, 0.8, 0.9, 0.1, 0.6, 0.7, 1]

bester_match=0
person_am_besten=""

i=0

repeat len(gefaellt_mir):
    ich = gefaellt_mir[i]
    er = gefaellt_ihm[i]
    match=(ich+er)-abs(ich-er)
    if match>bester_match:
        bester_match=match
        person_am_besten=dating_mann[i]
    
    i+=1
    
print(person_am_besten, "score", bester_match)
    
    