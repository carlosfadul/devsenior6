class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

persona1 = Persona("Juan")
#print(persona1.nombre)
print(persona1.get_nombre())  # Output: Juan
persona1.set_nombre("Pedro")
print(persona1.get_nombre())  # Output: Pedro
p1 = Persona("Maria")
print(p1.get_nombre())  # Output: Maria

