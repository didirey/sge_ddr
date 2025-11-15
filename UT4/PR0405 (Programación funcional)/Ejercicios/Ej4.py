def mas_de_cinco_letras(p):
    return len(p) > 5

def a_mayusculas(p):
    return p.upper()

palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

palabras_largas = filter(mas_de_cinco_letras, palabras)
palabras_mayusculas = list(map(a_mayusculas, palabras_largas))
print("Palabras con más de 5 letras en mayúsculas:")
print(palabras_mayusculas)
