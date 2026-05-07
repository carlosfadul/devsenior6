edad = int(input("Ingrese su edad: "))

"""
si edad menor o igual a 5: primera infancia
    entre 6 y 11: infancia
entre 12 y 17: adolescencia
mayor o igual a 18 adulto
"""
if edad <= 5:
    print("Primera infancia")
elif edad >= 6 and edad <= 11:
    print("Infancia")
elif edad >= 12 and edad <= 17:
    print("Adolescencia")
else:
    print("Adulto")      
   