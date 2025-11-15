def puntuacion_final(puntos_base, bonus):
    # TU IMPLEMENTACIÓN AQUÍ
    pass


# ---------------------------
# TESTS
# ---------------------------

tests = []

# caso simple
tests.append(puntuacion_final([10], [False]) == 10)

# con bonus
tests.append(puntuacion_final([10], [True]) == 15)

# varios elementos sin bonus
tests.append(puntuacion_final([5,10,2], [False,False,False]) == 17)

# varios elementos con mezcla
# rondas:
# 5 +5 → 10
# 10 (sin bonus)
# 3 +5 → 8
# total = 28
tests.append(puntuacion_final([5,10,3], [True,False,True]) == 28)

# listas vacías
tests.append(puntuacion_final([], []) == 0)

# listas grandes
tests.append(puntuacion_final([1,1,1,1,1], [True,True,True,True,True]) == 1*5 + 5*5)


# ---------------------------
# CALCULO DE NOTA
# ---------------------------

total = len(tests)
ok = sum(tests)
nota = (ok/total)*0.8

print("Tests totales:", total)
print("Tests OK:", ok)
print("NOTA:", round(nota,2))
