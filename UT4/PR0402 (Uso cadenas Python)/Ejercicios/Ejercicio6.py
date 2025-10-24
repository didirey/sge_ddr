cadena_original = input("Introduce una cadena de texto: ")

cadena_invertida = ""

for caracter in cadena_original:
    if 'a' <= caracter <= 'z':
        caracter_invertido = caracter.upper()
    elif 'A' <= caracter <= 'Z':
        caracter_invertido = caracter.lower()
    else:
        caracter_invertido = caracter
    
    cadena_invertida += caracter_invertido

print(f"\nCadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")