cadena_original = input("Introduce una cadena de palabras separadas (ej: primera-palabra otra): ")

# Normalizar la cadena: reemplazar guiones por espacios y convertir a minúsculas
cadena_normalizada = cadena_original.replace('-', ' ').lower()

# Separar la cadena en una lista de palabras
palabras = cadena_normalizada.split()

if not palabras:
    camelCase = ""
else:
    # La primera palabra se mantiene completamente en minúsculas
    camelCase = palabras[0]

    # Procesar el resto de las palabras
    for palabra in palabras[1:]:
        # Capitalizar (poner en mayúscula solo la primera letra) y añadir
        camelCase += palabra.capitalize()

print(f"\nCadena original: {cadena_original}")
print(f"Cadena en camelCase: {camelCase}")