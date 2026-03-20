def hunger_auf_schoggi():
    hunger = 1
    while hunger > 0.2:
        print(
            "Ich habe Hunger und esse noch etwas Schokolade (aktuell Hunger: "
            + str(round(hunger, 2))
            + ")"
        )


hunger_auf_schoggi()
