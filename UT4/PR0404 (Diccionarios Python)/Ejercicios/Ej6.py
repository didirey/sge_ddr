productos1 = {
    'manzana': 1.0,
    'banana': 2.0,
    'naranja': 1.5
}
productos2 = {
    'manzana': 1.5,
    'pera': 3.0,
    'banana': 1.0
}
print("Diccionario 1:")
print(productos1)
print("\nDiccionario 2:")
print(productos2)
print("\n")

productos_combinados = productos1.copy()  # Copiar el primer diccionario

for producto, precio in productos2.items():
    if producto in productos_combinados:
        # Si el producto ya existe, sumar los precios
        productos_combinados[producto] += precio
    else:
        # Si no existe, agregarlo
        productos_combinados[producto] = precio
print("Diccionario combinado (productos comunes sumados, únicos incluidos):")
print(productos_combinados)