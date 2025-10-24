scanner = str(input("Introduce una cadena de texto: ")).replace(" ", "")
opposite = scanner[::-1]

if opposite == scanner:
    print("Es palindromo")
else:
    print("No es palindromo")