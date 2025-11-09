persona = {
    'nombre': 'Michael',
    'edad': 30,
    'ciudad': 'Nueva York'
}
print("Diccionario original:")
print(persona)
print("\n")
# Intercambiar claves y valores usando comprensión de diccionarios
persona_invertida = {valor: clave for clave, valor in persona.items()}
print("Diccionario con claves y valores intercambiados:")
print(persona_invertida)