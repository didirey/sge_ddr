fruteria = {
    "Pera": 0.90,
    "Manzana": 1.00,
    "Mango": 1.10,
    "Sandia": 2.00,
    "Platano": 0.95,
}

fruta = str(input("Pregunta por una fruta: "))

if (fruta in fruteria):
    print(fruta + " cuesta " + str(fruteria[fruta]) + "$")
else:
    print("No tenemos esa fruta.")