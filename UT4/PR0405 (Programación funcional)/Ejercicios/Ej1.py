def es_par(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(es_par, numeros))
print("Números pares:")
print(numeros_pares)
