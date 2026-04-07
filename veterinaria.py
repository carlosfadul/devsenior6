from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_nombre(self):
        pass

class Veterinario(Persona):
    def mostrar_nombre(self):
        print(f"Veterinario: {self.nombre}")

    def atender(self):
        return f"{self.nombre} está atendiendo a una mascota."
    
class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}"
    
class Consulta:
    def __init__(self, mascota, motivo):
        self.mascota = mascota
        self.motivo = motivo
    
    def mostrar_consulta(self):
        return f"Consulta para {self.mascota.nombre} ({self.mascota.especie}) por: {self.motivo}"
    
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []
    
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print(f"Cliente: {self.nombre}")
        for mascota in self.mascotas:
            print(mascota.mostrar_info())

cliente = Cliente("Ana")
mascota1 = Mascota("Trosky", "Canino")
mascota2 = Mascota("Michin", "Felino")

cliente.agregar_mascota(mascota1)
cliente.agregar_mascota(mascota2)

veterinario1 = Veterinario("Jhon García")

consulta1 = Consulta(mascota1, "Vacunación")

cliente.mostrar_mascotas()

print(veterinario1.atender())
print(consulta1.mostrar_consulta())
