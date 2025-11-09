from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

# Aplanar con comprensión de listas
numeros_planos = [n for sublista in numeros for n in sublista]

# Filtrar y reducir
numeros_positivos = filter(lambda n: n > 0, numeros_planos)
suma_positivos = reduce(lambda x, y: x + y, numeros_positivos, 0)

print("Suma de todos los números positivos:")
print(suma_positivos)
