celsius = [0, 20, 37, 100]

def celsius_to_fahrenheit(x):
    return x * 2

nuevo = map(celsius_to_fahrenheit ,celsius)
print(nuevo)
