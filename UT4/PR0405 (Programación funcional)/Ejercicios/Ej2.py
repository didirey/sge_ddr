celsius = [0, 20, 37, 100]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Temperaturas en Fahrenheit:")
print(fahrenheit)