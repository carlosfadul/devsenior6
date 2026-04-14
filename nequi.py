class Usuario:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Documento: {self.documento}"
        
class ClientePremium(Usuario):
    def __init__(self, nombre, documento, beneficios):
        super().__init__(nombre, documento)
        self.beneficios = beneficios
    
    def mostrar_beneficios(self):
        return f"{self.nombre} tiene beneficios premium: {self.beneficios}"
    
class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
    
    def mostrar_transaccion(self):
        return f"Tipo: {self.tipo} Monto: {self.monto}"
    
class Cuenta:
    def __init__(self, numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.transacciones = [] #Composicion: Cuenta tiene una lista de Transacciones

    def depositar(self, monto):
        self.saldo += monto
        self.transacciones.append(Transaccion("Depósito", monto))
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(Transaccion("Retiro", monto))
        else:
            print("Saldo insuficiente para retirar.")
    
    def mostrar_historial(self):
        print(f"Historial de transacciones para la cuenta {self.numero_cuenta}:")
        for transaccion in self.transacciones:
            print(transaccion.mostrar_transaccion())

    def mostrar_saldo(self):
        print(f"Saldo actual de la cuenta {self.numero_cuenta}: {self.saldo}")

#Ensayis

usuario = Usuario("Carlos", "12345")
cliente_premium = ClientePremium("Ana", "67890", "Descuentos exclusivos")

cuenta1 = Cuenta("001", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.mostrar_saldo()
cuenta1.mostrar_historial()

print(usuario.mostrar_info())
print(cliente_premium.mostrar_info())

print(cliente_premium.mostrar_beneficios())