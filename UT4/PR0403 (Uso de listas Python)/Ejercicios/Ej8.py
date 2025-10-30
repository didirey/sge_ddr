from collections import Counter

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

conteo_letras = Counter()

# 1. Normalizar y concatenar todos los nombres
cadena_nombres = "".join(nombres).lower()

# 2. Iterar y contar, normalizando tildes a su base (a -> a, á -> a)
for caracter in cadena_nombres:
    if 'a' <= caracter <= 'z' or caracter in 'ñáéíóú':
        # Normalización de tildes
        if caracter in 'á':
            conteo_letras['a'] += 1
        elif caracter in 'é':
            conteo_letras['e'] += 1
        elif caracter in 'í':
            conteo_letras['i'] += 1
        elif caracter in 'ó':
            conteo_letras['o'] += 1
        elif caracter in 'ú':
            conteo_letras['u'] += 1
        else:
            conteo_letras[caracter] += 1

print("Conteo de cada letra del abecedario (normalizado a minúsculas):")

letras_encontradas = sorted(conteo_letras.keys())

for letra in letras_encontradas:
    print(f"La letra '{letra}' se repite {conteo_letras[letra]} veces.")