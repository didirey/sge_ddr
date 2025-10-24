cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

# Preprocesamiento: eliminar espacios y convertir a minúsculas
cadena1_limpia = "".join(cadena1.lower().split())
cadena2_limpia = "".join(cadena2.lower().split())

# Verificar si tienen la misma longitud
if len(cadena1_limpia) != len(cadena2_limpia):
    es_anagrama = False
else:
    # Convertir cada cadena limpia en una lista de caracteres y ordenarlas
    lista1_ordenada = sorted(list(cadena1_limpia))
    lista2_ordenada = sorted(list(cadena2_limpia))
    
    # Si las listas ordenadas son idénticas, las cadenas son anagramas
    if lista1_ordenada == lista2_ordenada:
        es_anagrama = True
    else:
        es_anagrama = False

print(f"\nCadena 1: {cadena1}")
print(f"Cadena 2: {cadena2}")

if es_anagrama:
    print("Las cadenas son anagramas")
else:
    print("Las cadenas NO son anagramas.")