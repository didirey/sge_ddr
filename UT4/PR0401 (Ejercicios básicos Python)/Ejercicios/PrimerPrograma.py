read = input("¿Que ciclo estas cursando? >")

print(
    "Desarrollo de Aplicaciones Multiplataforma" if read == "DAM" else
    "Desarrollo de Aplicaciones Web" if read == "DAW" else
    "No estas cursando ningun ciclo"
)