cadena_original = input("Introduce una cadena de texto: ")

rotaciones_str = input("Introduce el número de rotaciones a la izquierda: ")
rotaciones = int(rotaciones_str)

n = len(cadena_original)
rotaciones_efectivas = rotaciones % n

if n == 0 or rotaciones_efectivas == 0:
    cadena_rotada = cadena_original
else:
    parte_inicio = cadena_original[:rotaciones_efectivas]
    parte_final = cadena_original[rotaciones_efectivas:]
    cadena_rotada = parte_final + parte_inicio

print(f"\nCadena original: {cadena_original}")
print(f"Rotaciones: {rotaciones}")
print(f"Cadena rotada: {cadena_rotada}")