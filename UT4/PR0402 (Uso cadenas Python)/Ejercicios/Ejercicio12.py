cadena_original = input("Introduce una cadena para codificar: ")

if not cadena_original:
    cadena_codificada = ""
else:
    cadena_codificada = ""
    n = len(cadena_original)
    i = 0

    while i < n:
        caracter_actual = cadena_original[i]
        conteo = 1
        
        j = i + 1
        while j < n and cadena_original[j] == caracter_actual and conteo < 9:
            conteo += 1
            j += 1
        
        cadena_codificada += caracter_actual + str(conteo)
        i = j

print(f"\nCadena original: {cadena_original}")
print(f"Cadena codificada (RLE): {cadena_codificada}")