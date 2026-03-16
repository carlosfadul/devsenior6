# ==========================================
# SOLUCIÓN COMPLETA - SISTEMA DE ESTUDIANTES
# ==========================================

def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            return nombre
        else:
            print("Error: el nombre no puede estar vacío.")


def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad > 0:
                return edad
            else:
                print("Error: la edad debe ser mayor que 0.")
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def solicitar_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero_nota} (0.0 a 5.0): "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Error: la nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Error: debe ingresar un número válido.")


def registrar_estudiante():
    print("\n--- Registro de estudiante ---")
    nombre = solicitar_nombre()
    edad = solicitar_edad()
    nota1 = solicitar_nota(1)
    nota2 = solicitar_nota(2)
    nota3 = solicitar_nota(3)

    return nombre, edad, nota1, nota2, nota3


def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"


def mostrar_estudiante(estudiante):
    print("\n===== RESULTADO DEL ESTUDIANTE =====")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']} años")
    print(f"Nota 1: {estudiante['nota1']:.2f}")
    print(f"Nota 2: {estudiante['nota2']:.2f}")
    print(f"Nota 3: {estudiante['nota3']:.2f}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
    print(f"Estado académico: {estudiante['estado']}")


def mostrar_todos_los_estudiantes(lista_estudiantes):
    print("\n===== LISTADO DE ESTUDIANTES =====")

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for i, estudiante in enumerate(lista_estudiantes, start=1):
        print(
            f"{i}. {estudiante['nombre']} - "
            f"Edad: {estudiante['edad']} - "
            f"Promedio: {estudiante['promedio']:.2f} - "
            f"Estado: {estudiante['estado']}"
        )


def mostrar_resumen_final(lista_estudiantes):
    print("\n===== RESUMEN FINAL =====")
    total_estudiantes = len(lista_estudiantes)
    print(f"Total de estudiantes registrados: {total_estudiantes}")

    if total_estudiantes > 0:
        suma_promedios = 0
        for estudiante in lista_estudiantes:
            suma_promedios += estudiante["promedio"]

        promedio_general = suma_promedios / total_estudiantes
        print(f"Promedio general del grupo: {promedio_general:.2f}")
    else:
        print("Promedio general del grupo: 0.00")


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Salir")


def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre, edad, nota1, nota2, nota3 = registrar_estudiante()
            promedio = calcular_promedio(nota1, nota2, nota3)
            estado = evaluar_estado(promedio)

            estudiante = {
                "nombre": nombre,
                "edad": edad,
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3,
                "promedio": promedio,
                "estado": estado
            }

            estudiantes.append(estudiante)
            mostrar_estudiante(estudiante)

        elif opcion == "2":
            mostrar_todos_los_estudiantes(estudiantes)

        elif opcion == "3":
            print("\nSaliendo del sistema...")
            mostrar_resumen_final(estudiantes)
            print("Programa finalizado.")
            break

        else:
            print("Error: opción no válida. Intente nuevamente.")


# Punto de entrada del programa
main()