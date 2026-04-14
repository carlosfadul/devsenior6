from abc import ABC, abstractmethod

# Clase abstracta y herencia

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        

    @abstractmethod
    def calcular_salario(self):
        pass

class Mesero(Empleado):
    def calcular_salario(self):
        return 1200
    
class Chef(Empleado):
    def calcular_salario(reslf):
        return 2000
    
#Cliente y agregación con Pedido

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []
        
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

#Plato
class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#Pedido y composición con Plato

class Pedido:
    def __init__(self, cliente):
        self.estado = "pendiente"
        self.platos = []
        self.cliente = cliente
        self.mesero = None

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def asignar_mesero(self, mesero):
        self.mesero = mesero

    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)
    
#Restaurante agregacion empleados y clientes

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

class MetodoPago(ABC):
    def __init__(self, monto):
        self.monto = monto

    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo procesado por {monto}."
    
class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta procesado por {monto}."
    
#Factura y asociación con MetodoPago
class Factura:
    def __init__(self, pedido, impuestos = 0.19, descuento = 0):
        self.pedido = pedido
        self.impuestos = impuestos
        self.descuento = descuento
        
    def calcular_total(self):
        subtotal = self.pedido.calcular_total()
        total = subtotal + (subtotal * self.impuestos) - self.descuento
        return total
    
    def pagar(self, metodo_pago: MetodoPago):
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)
    
restaurante = Restaurante("El Buen Sabor")
mesero = Mesero("Juan")
chef = Chef("Maria")

restaurante.agregar_empleado(mesero)
restaurante.agregar_empleado(chef)

cliente = Cliente("Carlos")
restaurante.agregar_cliente(cliente)

plato1 = Plato("Pasta", 10)
plato2 = Plato("Bandeja paisa", 15)

pedido = Pedido(cliente)
pedido.agregar_plato(plato1)
pedido.agregar_plato(plato2)
pedido.asignar_mesero(mesero)

cliente.agregar_pedido(pedido)

factura = Factura(pedido, impuestos=0.19, descuento=5)
print("Total a pagar:", factura.calcular_total())

pago = PagoTarjeta(factura.calcular_total())
print(factura.pagar(pago))