j1_points = 0
j2_points = 0

while (j1_points < 5) and (j2_points < 5):
    j1 = input("Di la elección del jugador 1: ").lower()
    j2 = input("Di la elección del jugador 2: ").lower()

    match j1:
        case "piedra":
            res = ("Gana jugador 1" if j2 in ["lagarto", "tijeras"] else
                "Gana jugador 2" if j2 in ["papel", "spock"] else
                "Empate")
        case "papel":
            res = ("Gana jugador 1" if j2 in ["piedra"] else
                "Gana jugador 2" if j2 in ["tijeras", "lagarto"] else
                "Empate")
        case "tijeras":
            res = ("Gana jugador 1" if j2 in ["lagarto", "papel"] else
                "Gana jugador 2" if j2 in ["piedra", "spock"] else
                "Empate")
        case "lagarto":
            res = ("Gana jugador 1" if j2 in ["papel", "spock"] else
                "Gana jugador 2" if j2 in ["tijeras"] else
                "Empate")
        case "spock":
            res = ("Gana jugador 1" if j2 in ["tijeras", "piedra"] else
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

if j1_points == 5:
    print("\n Jugador 1 gana!!")
elif j2_points ==5:
    print("\n Jugador 2 gana!!")