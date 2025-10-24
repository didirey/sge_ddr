cadena_codificada = input("Introduce una cadena codificada (ej: a2r1o1n1): ")

cadena_decodificada = ""
i = 0
n = len(cadena_codificada)

while i < n:
    caracter = cadena_codificada[i]
    
    # El siguiente carácter debe ser el contador
    if i + 1 < n:
        contador_str = cadena_codificada[i + 1]
        
        # Asumiendo que el contador es un dígito
        contador = int(contador_str)
        
        # Añadir el carácter repetido el número de veces indicado
        cadena_decodificada += caracter * contador
        
        # Saltar al siguiente par de carácter/contador
        i += 2
    else:
        # Manejo de error si la cadena termina en un carácter sin contador
        cadena_decodificada += caracter
        i += 1

print(f"\nCadena codificada: {cadena_codificada}")
print(f"Cadena decodificada: {cadena_decodificada}")