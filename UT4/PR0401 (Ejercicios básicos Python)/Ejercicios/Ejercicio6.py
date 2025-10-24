result = 0

def convert_units(number, measurement, convert):

    global result # Esto se asgura de que estamos usando la variable que esta afuera de el metodo. 'result'

    match measurement:
        case "mm":
            if convert == "cm":
                result = number / 10
            elif convert == "m":
                result = number / 1000
            elif convert == "km":
                result = number / 1000000
        case "cm":
            if convert == "mm":
                result = number * 10
            elif convert == "m":
                result = number / 100
            elif convert == "km":
                result = number / 100000
        case "m":
            if convert == "mm":
                result = number * 1000
            elif convert == "cm":
                result = number * 100
            elif convert == "km":
                result = number / 1000
        case "km":
            if convert == "mm":
                result = number * 1000000
            elif convert == "cm":
                result = number * 100000
            elif convert == "m":
                result = number * 1000
        case _:
            result = "Unidad de medida no válida"

number = int(input("Ingrese un número entero: "))
measurement = str(input("Ingrese la unidad de medida del número (mm, cm, m, km): "))
convert = str(input("Ingrese la unidad a la que quiera convertir (mm, cm, m, km): "))

convert_units(number, measurement, convert)

print("")
print(f"{number} {measurement} son {result} {convert}")

