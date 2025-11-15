from functools import reduce

def calcular_medias(alumnos:dict):
    for v1, v2 in alumnos.items():
        name = v1
        grades1 = v2
        for nota in grades1:
            grades2 = []
            grades2[nota]

    suma = (reduce(lambda x, y: x + y, grades2)) 
    division = grades2.len()

    media = suma / division

    return {"nombre": name, "media": media}
    pass


# ---------------------------
# TESTS
# ---------------------------

tests = []

# caso simple
entrada1 = [{'nombre':'Ana', 'notas':[5,8,7]}]
salida1 = [{'nombre':'Ana', 'media':(5+8+7)/3}]
tests.append( calcular_medias(entrada1) == salida1 )

# varios alumnos
entrada2 = [
    {'nombre':'A','notas':[0,10]},
    {'nombre':'B','notas':[10,10,10]},
]
salida2 = [
    {'nombre':'A','media':5},
    {'nombre':'B','media':10},
]
tests.append( calcular_medias(entrada2) == salida2 )

# notas vacías (media = 0)
entrada3 = [{'nombre':'X','notas':[]}]
salida3 = [{'nombre':'X','media':0}]
tests.append( calcular_medias(entrada3) == salida3 )

# lista vacía
entrada4 = []
salida4 = []
tests.append( calcular_medias(entrada4) == salida4 )

# orden de salida igual que entrada
entrada5 = [{'nombre':'N1','notas':[1,1]}, {'nombre':'N2','notas':[2,2]}]
salida5 = [{'nombre':'N1','media':1}, {'nombre':'N2','media':2}]
tests.append( calcular_medias(entrada5) == salida5 )


# ---------------------------
# CALCULO DE NOTA
# ---------------------------

total = len(tests)
ok = sum(tests)
nota = (ok/total)*0.8

print("Tests totales:", total)
print("Tests OK:", ok)
print("NOTA:", round(nota,2))
