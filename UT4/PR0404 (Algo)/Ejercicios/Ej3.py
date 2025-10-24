frase = str(input("Escribe una frase: "))

palabras = frase.split()

frecuencia = {}

for palabra in palabras:
    palabra = palabra.lower()

    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frencuencia de la frase:")

for palabra, conteo in frecuencia.items():
        print(f"{palabra}: {conteo}")