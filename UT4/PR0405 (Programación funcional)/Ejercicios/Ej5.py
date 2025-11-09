from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = filter(lambda n: n % 2 == 0, numeros)
producto = reduce(lambda x, y: x * y, numeros_pares)
print("Producto de los números pares:")
print(producto)
