scanner = str(input("Introduce una frase: ")).lower().strip()
vocales = ["a", "e", "i", "o", "u"]
num_vocales = 0
num_consonantes = 0

scanner = scanner.replace(" ", "")

for char in scanner:
    if (char in vocales):
        num_vocales = num_vocales + 1
    else:
        num_consonantes = num_consonantes + 1

print("Numero vocales: ", num_vocales, "Numero consonantes: ", num_consonantes)
