a = 1
b = 1
n = int(input("Introduce la cantidad de números para la secuencia de Fibonacci: "))
c = 0

if n >= 1:
    print(a)
    c = 1
if n >= 2:
    print(b)
    c = 2

while c < n:
    resultado = a + b
    print(resultado)
    a = b
    b = resultado
    c += 1