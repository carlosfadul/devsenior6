day = input("Ingrese un número (1-7): ")
match day:
  case "1":
    print("Monday")
  case "2":
    print("Tuesday")
  case "3":
    print("Wednesday")
  case "4":
    print("Thursday")
  case "5":
    print("Friday")
  case "6":
    print("Saturday")
  case "7":
    print("Sunday")
  case _:  
    print("Number not valid")   

"""
preguntar al usuario un animal (perro, gato, pez)
si el animal es perro imprimir "Guau"
si el animal es gato imprimir "Miau"    
si el animal es pez imprimir "Blub"
y si el animal no es ninguno de esos imprimir "Animal no reconocido"
"""