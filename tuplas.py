frutas = ("manzana", "banana", "naranja","banana")
print(frutas)

copia = list(frutas)
copia.remove("naranja")
frutas = tuple(copia)
print(frutas)