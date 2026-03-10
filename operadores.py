"""
vamos a calcular el valor a pagar a un empleado por su trabajo de la semana
le vamos a preguntar al usuario cuantas horas trabajo el empleado y cuanto gana por hora
y al final le vamos a mostrar el valor a pagar al empleado por su trabajo de la semana
"""
# ahora vamos a hacer el calculo de la nomina de los TRES EMPLEADOS DE LA EMPRESA

horas1 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora1 = int(input("Cuanto gana por hora? "))
sueldo1 = horas1 * pago_por_hora1

horas2 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora2 = int(input("Cuanto gana por hora? "))
sueldo2 = horas2 * pago_por_hora2

horas3 = float(input("Cuantas horas trabajo el empleado? "))
pago_por_hora3 = int(input("Cuanto gana por hora? "))
sueldo3 = horas3 * pago_por_hora3

nomina = sueldo1 + sueldo2 + sueldo3
print("El valor a pagar a los empleados por su trabajo de la semana es: ", nomina)