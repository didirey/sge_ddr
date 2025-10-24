cadena_original = input("Introduce una cadena de texto: ")

cadena_sin_duplicados = ""
caracteres_vistos = set()

for caracter in cadena_original:
    if caracter not in caracteres_vistos:
        cadena_sin_duplicados += caracter
        caracteres_vistos.add(caracter)

print(f"Cadena original: {cadena_original}")
print(f"Cadena sin duplicados: {cadena_sin_duplicados}")