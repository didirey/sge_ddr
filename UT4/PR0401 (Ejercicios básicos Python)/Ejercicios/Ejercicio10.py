
entrada = input("Introduce un número entero: ")
numero = int(entrada)

es_primo = True

if numero <= 1:
    es_primo = False
elif numero == 2:
    es_primo = True
elif numero % 2 == 0:
    es_primo = False
else:
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            es_primo = False
            break
        i += 2

if es_primo:
    print(f"\nEl número {numero} si es primo")
else:
    print(f"\nEl número {numero} no es primo.")