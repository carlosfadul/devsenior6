"""
for x in range(1, 11):
    print(x)

for x in range(5):
    print(x)

for x in range(1, 11, 2):
    print(x)


texto = "Python es muy bacano"
for letra in texto:
    print(letra)
"""
"""
3x1=3
3x2=6
3x3=9
3x4=12
"""
tabla = int(input("Ingrese la tabla de multiplicar que desea: "))
for x in range(1, 11):
    print(tabla, "x", x, "=",  x*tabla)
print("hola")