from functools import reduce

def calcular_total(precios:list, cupon:str):

    # Usar reduce con una función lambda para sumar acumulativamente
    suma_total = float(reduce(lambda x, y: x + y, precios))

    if suma_total > 50:
        suma_total = suma_total * 0.05
    
    if cupon == "DESCUENTO10":
        suma_total = suma_total * 0.10

    return suma_total

print(calcular_total([10.0, 20.0, 5.0], "SIN_CUPON"))