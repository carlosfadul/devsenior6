class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  

    def ladrar(self):
        return "¡Guau!" 

    def rascarse(self):
        print("¡Me estoy rascando!")

perro1 = Perro("Trosky", 5)
perrito = Perro("Firulais", 3)
print(perro1.nombre, perro1.edad)
print(perrito.nombre, perrito.edad)
print(perro1.ladrar())
print(perrito.ladrar())
perro1.rascarse()
perrito.rascarse()