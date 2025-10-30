numeros_con_duplicados = [1, 5, 3, 2, 1, 4, 3, 5, 5, 2]

# Convertir la lista a un conjunto (set) para eliminar duplicados
elementos_unicos_set = set(numeros_con_duplicados)

# Convertir el conjunto de vuelta a una lista para mostrar el resultado final
lista_sin_duplicados = list(elementos_unicos_set)

print(lista_sin_duplicados)