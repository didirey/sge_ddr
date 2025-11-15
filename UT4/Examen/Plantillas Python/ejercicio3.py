import random
import string

def generar_password(longitud, incluir_numeros, incluir_simbolos):
    # TU IMPLEMENTACIÓN AQUI
    pass


# ---------------------------
# FUNCIONES AUXILIARES DE TEST
# ---------------------------

def solo_letras(s):
    return all(c in string.ascii_letters for c in s)

def tiene_numero(s):
    return any(c in string.digits for c in s)

def tiene_simbolo(s):
    return any(c in string.punctuation for c in s)


# ---------------------------
# TESTS
# ---------------------------

tests = []

p1 = generar_password(8, False, False)
tests.append(len(p1)==8 and solo_letras(p1))

p2 = generar_password(12, True, False)
tests.append(len(p2)==12 and tiene_numero(p2) and not tiene_simbolo(p2))

p3 = generar_password(16, True, True)
tests.append(len(p3)==16 and tiene_numero(p3) and tiene_simbolo(p3))

p4 = generar_password(4, True, False)
tests.append(len(p4)==4)

p5 = generar_password(1, False, False)
tests.append(len(p5)==1 and solo_letras(p5))


# ---------------------------
# CALCULO DE NOTA
# ---------------------------

total = len(tests)
ok = sum(tests)
nota = (ok/total)*0.8

print("Tests totales:", total)
print("Tests OK:", ok)
print("NOTA:", round(nota,2))
