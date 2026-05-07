"""
pedir al usuario que ingrese notas entre 0 y 10, 
hasta que ingrese -1 para finalizar. 
Luego, mostrar el promedio de las notas ingresadas.
"""
notas = []
while True:    
    nota = float(input("Ingrese una nota entre 0 y 10 (o -1 para finalizar): "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. Por favor, ingrese una nota entre 0 y 10.")

if notas:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas ingresadas es: {promedio}")
else:
    print("No se ingresaron notas válidas.")