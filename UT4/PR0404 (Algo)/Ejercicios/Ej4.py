asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

run = True

print("=== Base de Datos Matriculados ===")

print("")
print("1- Listar estudiantes de asignatura")
print("2- Matricular estudiante en asignatura")
print("3- Dar de baja un estudiante")
print("4- Salir")
print("")

while(run):
    scanner = str(input("Introduce un numero para escoger una opción  >"))

    match scanner:
        case "1":
            print("")
            print("= Listado =")
            print("")
            for asignatura, estudiante in asignaturas.items():
                print(f"Asignatura {asignatura}")
                print(f"Estudiantes: {estudiante}")
                print("")
        case "2":
            print("")
            print("= Matricular =")
            print("")
            estudiante = str(input("Introduce el nombre del estudiante  >"))
            asignatura = str(input("Introduce la asignatura en la que matricularlo  >"))
            if (asignatura in asignaturas):
                asignaturas[asignatura].append(estudiante)
            else:
                asignaturas[asignatura] = estudiante
            print("")
            print(f"Estudiante {estudiante} matriculado en {asignatura}")
            print("")
        case "3":
            print("")
            print("= Borrar =")
            print("")
            estudianteIn = str(input("Introduce el nombre del estudiante  >"))
            asignaturaIn = str(input("Introduce la asginatura  en la que darlo de baja  >"))
            for asignatura, estudiante in asignaturas:
                if (asignaturaIn == asignatura and estudianteIn == estudiante):
                    estudiante(estudianteIn).remove
            print("")
        case "4":
            run = False
            print("Saliendo del programa...")
            print("==================================")
        case _:
            print("")
            print("Opcion no valida")
            print("")
            

