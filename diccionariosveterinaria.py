# ============================================================
# SISTEMA DE GESTIÓN DE VETERINARIA
# Diccionarios anidados
# Sin funciones y sin archivos
# ============================================================

# Diccionario principal
# Cada cliente será una clave del diccionario
# Dentro de cada cliente se guardará su teléfono y sus mascotas
veterinaria = {}

opcion = ""

while opcion != "8":

    print("\n========== MENÚ VETERINARIA ==========")
    print("1. Agregar cliente")
    print("2. Agregar mascota a un cliente")
    print("3. Mostrar todos los clientes y sus mascotas")
    print("4. Buscar una mascota")
    print("5. Calcular peso promedio de mascotas de un cliente")
    print("6. Encontrar la mascota más pesada")
    print("7. Eliminar una mascota")
    print("8. Eliminar un cliente")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # --------------------------------------------------------
    # 1. Agregar cliente
    # --------------------------------------------------------
    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            print("El cliente ya existe.")
        else:
            telefono = input("Ingrese el teléfono del cliente: ")

            veterinaria[nombre_cliente] = {
                "telefono": telefono,
                "mascotas": {}
            }

            print("Cliente agregado correctamente.")

    # --------------------------------------------------------
    # 2. Agregar mascota a un cliente
    # --------------------------------------------------------
    elif opcion == "2":
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")

            if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                print("Esta mascota ya está registrada para este cliente.")
            else:
                especie = input("Ingrese la especie de la mascota: ")
                edad = int(input("Ingrese la edad de la mascota: "))
                peso = float(input("Ingrese el peso de la mascota en kg: "))

                veterinaria[nombre_cliente]["mascotas"][nombre_mascota] = {
                    "especie": especie,
                    "edad": edad,
                    "peso": peso
                }

                print("Mascota agregada correctamente.")
        else:
            print("El cliente no existe.")

    # --------------------------------------------------------
    # 3. Mostrar todos los clientes y sus mascotas
    # --------------------------------------------------------
    elif opcion == "3":
        if len(veterinaria) == 0:
            print("No hay clientes registrados.")
        else:
            print("\n========== LISTADO GENERAL ==========")

            for cliente in veterinaria:
                print("\nCliente:", cliente)
                print("Teléfono:", veterinaria[cliente]["telefono"])

                if len(veterinaria[cliente]["mascotas"]) == 0:
                    print("Mascotas: No tiene mascotas registradas.")
                else:
                    print("Mascotas:")

                    for mascota in veterinaria[cliente]["mascotas"]:
                        especie = veterinaria[cliente]["mascotas"][mascota]["especie"]
                        edad = veterinaria[cliente]["mascotas"][mascota]["edad"]
                        peso = veterinaria[cliente]["mascotas"][mascota]["peso"]

                        print("-", mascota, "|", especie, "|", edad, "años |", peso, "kg")

    # --------------------------------------------------------
    # 4. Buscar una mascota
    # --------------------------------------------------------
    elif opcion == "4":
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")

            if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                mascota = veterinaria[nombre_cliente]["mascotas"][nombre_mascota]

                print("\nInformación de la mascota:")
                print("Nombre:", nombre_mascota)
                print("Especie:", mascota["especie"])
                print("Edad:", mascota["edad"], "años")
                print("Peso:", mascota["peso"], "kg")
                print("Propietario:", nombre_cliente)
            else:
                print("La mascota no está registrada para este cliente.")
        else:
            print("El cliente no existe.")

    # --------------------------------------------------------
    # 5. Calcular peso promedio de mascotas de un cliente
    # --------------------------------------------------------
    elif opcion == "5":
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            mascotas = veterinaria[nombre_cliente]["mascotas"]

            if len(mascotas) == 0:
                print("Este cliente no tiene mascotas registradas.")
            else:
                suma_pesos = 0

                for mascota in mascotas:
                    suma_pesos = suma_pesos + mascotas[mascota]["peso"]

                promedio = suma_pesos / len(mascotas)

                print("El peso promedio de las mascotas de", nombre_cliente, "es:", round(promedio, 2), "kg")
        else:
            print("El cliente no existe.")

    # --------------------------------------------------------
    # 6. Encontrar la mascota más pesada de toda la veterinaria
    # --------------------------------------------------------
    elif opcion == "6":
        if len(veterinaria) == 0:
            print("No hay clientes registrados.")
        else:
            mascota_mas_pesada = ""
            cliente_mascota = ""
            peso_mayor = -1

            for cliente in veterinaria:
                for mascota in veterinaria[cliente]["mascotas"]:
                    peso = veterinaria[cliente]["mascotas"][mascota]["peso"]

                    if peso > peso_mayor:
                        peso_mayor = peso
                        mascota_mas_pesada = mascota
                        cliente_mascota = cliente

            if mascota_mas_pesada != "":
                print("La mascota más pesada es:", mascota_mas_pesada)
                print("Peso:", peso_mayor, "kg")
                print("Propietario:", cliente_mascota)
            else:
                print("No hay mascotas registradas.")

    # --------------------------------------------------------
    # 7. Eliminar una mascota
    # --------------------------------------------------------
    elif opcion == "7":
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            nombre_mascota = input("Ingrese el nombre de la mascota a eliminar: ")

            if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                del veterinaria[nombre_cliente]["mascotas"][nombre_mascota]
                print("Mascota eliminada correctamente.")
            else:
                print("La mascota no existe para este cliente.")
        else:
            print("El cliente no existe.")

    # --------------------------------------------------------
    # 8. Eliminar un cliente
    # --------------------------------------------------------
    elif opcion == "8":
        nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ")

        if nombre_cliente in veterinaria:
            del veterinaria[nombre_cliente]
            print("Cliente eliminado correctamente.")
        else:
            print("El cliente no existe.")

    # --------------------------------------------------------
    # 9. Salir
    # --------------------------------------------------------
    elif opcion == "9":
        print("Saliendo del sistema...")

    # --------------------------------------------------------
    # Opción inválida
    # --------------------------------------------------------
    else:
        print("Opción inválida. Intente nuevamente.")