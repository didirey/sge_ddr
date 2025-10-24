cadena_original = input("Introduce una cadena de texto: ")

cadena_limpia = ""

for caracter in cadena_original:
    if caracter.isalnum() or caracter.isspace():
        cadena_limpia += caracter

print(f"\nCadena original: {cadena_original}")
print(f"Cadena sin no alfanuméricos: {cadena_limpia}")