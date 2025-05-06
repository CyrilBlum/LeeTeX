def beschreibe_wetter(temperatur):
    if temperatur >= 30:
        print("Es ist heiss")
    elif temperatur >= 20:
        print("Es ist warm")
    else:
        print("Es ist kühl")
    
beschreibe_wetter(33)