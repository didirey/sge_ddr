numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))

print(pares)