j1_points = 0
j2_points = 0

while (j1_points < 5) and (j2_points < 5):
    j1 = input("Di la elección del jugador 1: ").lower()
    j2 = input("Di la elección del jugador 2: ").lower()

    match j1:
        case "piedra":
            # Piedra gana a lagarto, tijeras
            res = ("Gana jugador 1" if j2 in ["lagarto", "tijeras"] else 
                # Piedra pierde con papel, spock
                "Gana jugador 2" if j2 in ["papel", "spock"] else
                "Empate")
        
        case "papel":
            # Papel gana a piedra, spock
            res = ("Gana jugador 1" if j2 in ["piedra", "spock"] else
                # Papel pierde con tijeras, lagarto
                "Gana jugador 2" if j2 in ["tijeras", "lagarto"] else
                "Empate")
        
        case "tijeras":
            # Tijeras gana a lagarto, papel
            res = ("Gana jugador 1" if j2 in ["lagarto", "papel"] else
                # Tijeras pierde con piedra, spock
                "Gana jugador 2" if j2 in ["piedra", "spock"] else
                "Empate")
        case "lagarto":
            # Lagarto gana a papel, spock
            res = ("Gana jugador 1" if j2 in ["papel", "spock"] else
                # Lagarto pierde con tijeras, piedra
                "Gana jugador 2" if j2 in ["tijeras", "piedra"] else
                "Empate")
        case "spock":
            # Spock gana a tijeras, piedra
            res = ("Gana jugador 1" if j2 in ["tijeras", "piedra"] else
                # Spock pierde con lagarto, papel
                "Gana jugador 2" if j2 in ["lagarto", "papel"] else
                "Empate")
            
    if "Gana jugador 1" in res:
        j1_points = j1_points + 1
        print("\n Gana punto jugador 1 \n")
    elif "Gana jugador 2" in res:
        j2_points = j2_points + 1
        print("\n Gana punto jugador 2 \n")
    elif "Empate" in res:
        print("\n Empate")

    print("J1 | J2")
    print("-------")
    print(j1_points, " | " , j2_points)
    print("-------\n")

if j1_points == 5:
    print("\n Jugador 1 gana!!")
elif j2_points ==5:
    print("\n Jugador 2 gana!!")