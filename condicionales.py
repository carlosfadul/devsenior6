"""
Escribir un programa en python que solicite al usuario un numero entre 1 y 7
si es 1 imprimir "Lunes"
si es 2 imprimir "Martes"
si es 3 imprimir "Miercoles"
si es 4 imprimir "Jueves"
si es 5 imprimir "Viernes"
si es 6 imprimir "Sabado"
si es 7 imprimir "Domingo"
y si el numero no esta entre 1 y 7 imprimir "Numero no valido"
"""
dia = int(input("Ingrese un número (1-7): "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Numero no valido")