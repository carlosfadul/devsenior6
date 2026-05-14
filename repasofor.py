sirenita = input("Ingrese una frase: ")
contador = 0
letra = input("Ingrese una letra para buscar en la frase: ")

for x in sirenita:
    print(x)
    if x == letra:
        print("Encontré una", letra)
        contador += 1
print("Fin del ciclo")
print("Número de '", letra, "' encontradas:", contador)