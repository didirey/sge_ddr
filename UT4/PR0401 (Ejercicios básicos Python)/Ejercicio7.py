from random import *

interval = randint(1, 100)
run = True

print("Adivina el número entre 1 y 100")

while run:
    number = int(input("Pon un número: "))
    if number < interval:
        print("El número es mayor ⬆️")
    elif number > interval:
        print("El número es menor ⬇️")
    else:
        print("Has acertado!!")
        run = False