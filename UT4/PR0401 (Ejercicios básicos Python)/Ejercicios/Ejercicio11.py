
entrada = input("Introduce un número entero no negativo (n): ")
n = int(entrada)

if n == 0:
    factorial = 1
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

print(f"\nEl factorial de {n} ({n}!) es: {factorial}")