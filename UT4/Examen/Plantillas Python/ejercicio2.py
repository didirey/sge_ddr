from functools import reduce

def calcular_total(precios:list, cupon:str):

    # Usar reduce con una función lambda para sumar acumulativamente
    suma_total = float(reduce(lambda x, y: x + y, precios, 0))

    if suma_total > 50:
        suma_total = suma_total * 0.95
    
    if cupon == "DESCUENTO10":
        suma_total = suma_total * 0.90

    return suma_total
    pass


# ---------------------------
# TESTS
# ---------------------------

tests = []

# subtotal <= 50, sin cupón
tests.append(abs(calcular_total([10, 15, 20], "SIN_CUPON") - 45) < 0.001)

# subtotal > 50, sin cupón → 5% descuento
# subtotal = 30 + 30 = 60 → 60 * 0.95 = 57
tests.append(abs(calcular_total([30,30], "SIN_CUPON") - 57) < 0.001)

# subtotal > 50 y cupón 10%
# subtotal = 60
# primero 5% → 57
# después 10% → 57 * 0.90 = 51.3
tests.append(abs(calcular_total([30,30], "DESCUENTO10") - 51.3) < 0.001)

# subtotal <= 50, cupón 10%
# 40 - 10% = 36
tests.append(abs(calcular_total([10, 15, 15], "DESCUENTO10") - 36) < 0.001)

# lista  vacía
tests.append(abs(calcular_total([], "SIN_CUPON") - 0) < 0.001)


# ---------------------------
# CALCULO DE NOTA
# ---------------------------

total = len(tests)
ok = sum(tests)
nota = (ok/total)*0.8

print("Tests totales:", total)
print("Tests OK:", ok)
print("NOTA:", round(nota,2))
