"""
Ejercicio: Sistema de Gestión de Estudiantes
Crea un programa que gestione las calificaciones de estudiantes usando diccionarios. 
El programa debe permitir:
Requisitos:
Estructura de datos: Usa un diccionario donde las claves sean los nombres de los estudiantes y
los valores sean listas de calificaciones.
Funcionalidades a implementar:
Agregar un nuevo estudiante (con una lista vacía de calificaciones)
Agregar calificaciones a un estudiante existente
Calcular el promedio de un estudiante
Mostrar todos los estudiantes con sus promedios
Encontrar el estudiante con el promedio más alto
Eliminar un estudiante
"""
estudiantes = {}
opcion = 0

menu = """
MENU PRINCIPAL
1. Agregar un nuevo estudiante
2. Agregar calificaciones a un estudiante existente
3. Calcular el promedio de un estudiante
4. Mostrar todos los estudiantes con sus promedios
5. Encontrar el estudiante con el promedio más alto
6. Eliminar un estudiante
7. Salir
"""
while opcion != 7:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            print("El estudiante ya existe.")
        else:
            estudiantes[nombre] = []
            print(f"Estudiante {nombre} agregado exitosamente.")
            print(estudiantes)
    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            calificacion = float(input("Ingrese la calificacion: "))
            estudiantes[nombre].append(calificacion)
            print(f"Calificacion {calificacion} agregada a {nombre}.")
        else:
            print("El estudiante no existe.")
        print(estudiantes)
    elif opcion == 3:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
           if len(estudiantes[nombre]) > 0:
                promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                print(f"El promedio de {nombre} es: {promedio:.2f}")
           else: 
                print(f"{nombre} no tiene calificaciones.")
        else:
            print("El estudiante no existe.")
    elif opcion == 4:
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("Estudiantes y sus promedios:")
            for nombre in estudiantes:
                if len(estudiantes[nombre]) > 0:
                    promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                    print(f"{nombre}: {promedio:.2f}")
                else:
                    print(f"{nombre}: No tiene calificaciones.")
    elif opcion == 5:
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            mejor_estudiante = ""
            mejor_promedio = -1
            for nombre in estudiantes:
                if len(estudiantes[nombre]) > 0:
                    promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                    if promedio > mejor_promedio:
                        mejor_promedio = promedio
                        mejor_estudiante = nombre
            print(f"El estudiante con el promedio más alto es {mejor_estudiante} con un promedio de {mejor_promedio:.2f}.")
    elif opcion == 6:
        nombre= input("Ingrese el nombre del estudiante a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print(f"Estudiante {nombre} eliminado exitosamente.")
        else:
            print("El estudiante no existe.")
    elif opcion == 7:
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

