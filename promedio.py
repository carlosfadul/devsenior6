# Programa que pide tres notas al usuario y calcula el promedio

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio de las tres notas es: {promedio:.2f}")
