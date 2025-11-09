from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Usar reduce con una función lambda para sumar acumulativamente
suma_total = reduce(lambda x, y: x + y, numeros)

print("Suma acumulativa:")
print(suma_total)
