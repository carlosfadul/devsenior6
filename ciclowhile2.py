menu = """
Restaurante el Buen Sabor
1. Hamburguesa - $20.000
2. Pizza - $15.000
3. Ensalada - $4.500
4. Salchipapa - $8.000
5. Perro Caliente - $12.000
6. Salir
"""
print(menu)
total = 0
totalHamburguesas = 0
cantidadHamburguesas = 0
totalPizzas = 0
cantidadPizzas = 0
totalEnsaladas = 0
cantidadEnsaladas = 0
totalSalchipapas = 0
cantidadSalchipapas = 0
totalPerrosCalientes = 0
cantidadPerrosCalientes = 0

opcion = 0
while opcion != 6:
    opcion = int(input("Ingrese una opción del menú: "))
    if opcion == 1:
        print("Has elegido Hamburguesa")
        total += 20000
        totalHamburguesas += 20000
        cantidadHamburguesas += 1
    elif opcion == 2:
        print("Has elegido Pizza")
        total += 15000
        totalPizzas += 15000
        cantidadPizzas += 1
    elif opcion == 3:
        print("Has elegido Ensalada")
        total += 4500
        totalEnsaladas += 4500
        cantidadEnsaladas += 1
    elif opcion == 4:
        print("Has elegido Salchipapa")
        total += 8000
        totalSalchipapas += 8000
        cantidadSalchipapas += 1
    elif opcion == 5:
        print("Has elegido Perro Caliente")
        total += 12000
        totalPerrosCalientes += 12000
        cantidadPerrosCalientes += 1

    elif opcion == 6:
        print("Pilas que no se vaya a volar sin pagar",total)
        print("Total hamburguesas:", totalHamburguesas, "cantidad Hamburguesas:", cantidadHamburguesas)
        print("Total pizzas:", totalPizzas, "cantidad Pizzas:", cantidadPizzas)
        print("Total ensaladas:", totalEnsaladas, "cantidad Ensaladas:", cantidadEnsaladas)
        print("Total salchipapas:", totalSalchipapas, "cantidad Salchipapas:", cantidadSalchipapas)
        print("Total perros calientes:", totalPerrosCalientes, "cantidad Perros Calientes:", cantidadPerrosCalientes)
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
        
    print(menu)
