"""
Vas a crear una clase llamada CuentaBancaria que simule una billetera digital como Nequi o Daviplata.

🔹 Requisitos
1. Atributos

Debes usar los tres niveles de acceso:

titular → Público
_historial → Protegido
__saldo → Privado
2. Constructor

Debe recibir:

titular
saldo inicial
3. Métodos obligatorios
🔹 Getters y Setters
Obtener saldo (NO acceso directo)
Modificar saldo SOLO con validación
🔹 Funcionalidades
depositar(monto)
retirar(monto)
ver_saldo()
ver_historial()
4. Validaciones
No permitir saldo negativo
No permitir retiros mayores al saldo
No permitir depósitos negativos
5. Prueba del sistema

En el programa principal:

Crear una cuenta
Depositar dinero
Retirar dinero
Mostrar saldo
Mostrar historial
"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._historial = []
        self.__saldo = 0
        self.depositar(saldo_inicial)

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, monto):
        if monto < 0:
            print("No se puede establecer un saldo negativo.")
            return
        self.__saldo = monto

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser positivo.")
            return
        self.__saldo += monto
        self._historial.append(f"Depósito: +{monto}")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
            return
        if monto > self.__saldo:
            print("No se puede retirar más de lo que tienes en la cuenta.")
            return
        self.__saldo -= monto
        self._historial.append(f"Retiro: -{monto}")

    def ver_saldo(self):
        print(f"Saldo actual: {self.get_saldo()}")

    def ver_historial(self):
        print("Historial de transacciones:")
        for transaccion in self._historial:
            print(transaccion)

def main():
    cuenta1 = CuentaBancaria("Carlos",50000)
    cuenta1.depositar(20000)
    cuenta1.retirar(10000)
    print(f"Esta es la cuenta de: {cuenta1.titular} y el saldo es {cuenta1.get_saldo()}  " )

    cuenta1.ver_saldo()

    cuenta1.ver_historial()


if __name__ == "__main__":
    main()