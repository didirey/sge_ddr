from collections import Counter

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]

vocales_conteo = Counter()
vocales = "aeiouáéíóú"

# Concatenamos todos los nombres en una sola cadena y los pasamos a minúsculas
cadena_nombres = "".join(nombres).lower()

# Contamos solo los caracteres que son vocales
for caracter in cadena_nombres:
    if caracter in vocales:
        # Normalizamos las vocales con tilde a su versión sin tilde para la cuenta
        if caracter in 'á':
            vocales_conteo['a'] += 1
        elif caracter in 'é':
            vocales_conteo['e'] += 1
        elif caracter in 'í':
            vocales_conteo['i'] += 1
        elif caracter in 'ó':
            vocales_conteo['o'] += 1
        elif caracter in 'ú':
            vocales_conteo['u'] += 1
        else:
            vocales_conteo[caracter] += 1

print("Conteo de cada vocal (incluyendo acentuadas en su base):")
for vocal, cantidad in sorted(vocales_conteo.items()):
    print(f"La vocal '{vocal}' se repite {cantidad} veces.")