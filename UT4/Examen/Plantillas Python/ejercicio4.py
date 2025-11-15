def a_segundos(tiempos):
    # TU IMPLEMENTACIÓN AQUÍ
    pass


# ---------------------------
# TESTS
# ---------------------------

tests = []

# caso simple
tests.append(a_segundos(["01:00"]) == [60])

# varios tiempos
tests.append(a_segundos(["03:20", "10:05"]) == [200, 605])

# tiempos con 0 minutos
tests.append(a_segundos(["00:45"]) == [45])

# tiempos con 0 segundos
tests.append(a_segundos(["02:00"]) == [120])

# lista vacía
tests.append(a_segundos([]) == [])

# varios mix
tests.append(a_segundos(["00:01","00:59","01:01"]) == [1,59,61])


# ---------------------------
# CALCULO DE NOTA
# ---------------------------

total = len(tests)
ok = sum(tests)
nota = (ok/total)*0.8

print("Tests totales:", total)
print("Tests OK:", ok)
print("NOTA:", round(nota,2))
