# Programa con menú de opciones que cuenta cuántos productos se piden de cada tipo

hamburguesa = 0
perro_caliente = 0
pizza = 0

while True:
    print("\nMenú de opciones:")
    print("1. Hamburguesa")
    print("2. Perro caliente")
    print("3. Pizza")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        hamburguesa += 1
        print("Has pedido una hamburguesa.")
    elif opcion == "2":
        perro_caliente += 1
        print("Has pedido un perro caliente.")
    elif opcion == "3":
        pizza += 1
        print("Has pedido una pizza.")
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 4.")

print("\nResumen de pedidos:")
print(f"Hamburguesas: {hamburguesa}")
print(f"Perros calientes: {perro_caliente}")
print(f"Pizzas: {pizza}")
