condition = True
while condition:
    number = int(input("Introduce un número impar: "))
    
    if number % 2 != 0:
        condition = False
    else:
        print("El número introducido no es impar. Inténtalo de nuevo.")

symbol = "*"
space = " "
i = 1

while (i <= number):
    print(space * ((number - i) // 2) + symbol)
    symbol += "**"
    i += 2
