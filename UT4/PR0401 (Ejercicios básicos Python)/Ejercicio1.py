condicion = True
while (condicion):
    scanner = input("Introduce el numero valido: ")

    if scanner.isdigit():
        print("Numero correcto")
        condicion = False
    else:
        print("Numero incorrecto, prueba otra vez")
