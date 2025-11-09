productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

num_categoria = 0
num_productos = 0

for categoria in productos:
    producto_actual = 0
    num_categoria = num_categoria + 1
    
    for producto in productos[categoria]:
        producto_actual = producto_actual + 1
        num_productos = num_productos + 1

    print(categoria + " tiene " + str(producto_actual) + " productos.")
        
print("\n Hay " + str(num_categoria) + " categorias en total.")
print("\n Hay " + str(num_productos) + " productos en total.")
print("\n")