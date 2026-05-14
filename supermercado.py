def validar_numero(mensaje, minimo, maximo, es_entero=False):
    """Valida que el usuario ingrese un número dentro de un rango"""
    while True:
        try:
            if es_entero:
                valor = int(input(mensaje))
            else:
                valor = float(input(mensaje))
            
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"❌ El valor debe estar entre {minimo} y {maximo}")
        except ValueError:
            print(f"❌ Ingresa un número válido")

def calcular_total_sin_descuento(num_productos):
    """Calcula el total de la compra sin descuento"""
    total = 0
    for i in range(num_productos):
        print(f"  Producto {i+1}:")
        precio = validar_numero("    Precio unitario: $", 0.01, 10000, False)
        cantidad = validar_numero("    Cantidad: ", 1, 100, True)
        subtotal = precio * cantidad
        total += subtotal
        print(f"    Subtotal: ${subtotal:.2f}")
    return total

def aplicar_descuento(total):
    """Aplica descuento según el total y retorna (total_final, porcentaje)"""
    if total > 500:
        porcentaje = 15
    elif total >= 200:
        porcentaje = 10
    elif total >= 100:
        porcentaje = 5
    else:
        porcentaje = 0
    
    descuento = total * porcentaje / 100
    total_final = total - descuento
    return total_final, porcentaje

def procesar_pago(total):
    """Procesa el pago y retorna el vuelto"""
    print(f"\n💰 Total a pagar: ${total:.2f}")
    
    while True:
        pago = validar_numero("¿Con cuánto paga? $", total, 10000, False)
        vuelto = pago - total
        if vuelto >= 0:
            return vuelto
        else:
            print("❌ El pago es insuficiente")

# Programa principal
print("="*50)
print("🏪 CAJA REGISTRADORA - SUPERMERCADO")
print("="*50)

num_clientes = validar_numero("¿Cuántos clientes atenderás? ", 1, 50, True)

# Acumuladores
total_vendido_dia = 0
clientes_pago_grande = 0
mayor_gasto = 0
menor_gasto = float('inf')
nombre_mayor = ""
nombre_menor = ""

# Ciclo principal
for cliente_num in range(1, num_clientes + 1):
    print(f"\n{'='*40}")
    print(f"🧑 CLIENTE {cliente_num}")
    print(f"{'='*40}")
    
    nombre = input("Nombre del cliente: ")
    
    num_productos = validar_numero("¿Cuántos productos compró? ", 1, 10, True)
    
    # Calcular total del cliente
    print("\n📦 REGISTRO DE PRODUCTOS:")
    total_bruto = calcular_total_sin_descuento(num_productos)
    
    # Aplicar descuento
    total_neto, descuento_aplicado = aplicar_descuento(total_bruto)
    
    # Mostrar resumen de compra
    print(f"\n📋 RESUMEN DE COMPRA:")
    print(f"  Subtotal: ${total_bruto:.2f}")
    if descuento_aplicado > 0:
        print(f"  Descuento: {descuento_aplicado}%")
    print(f"  Total: ${total_neto:.2f}")
    
    # Procesar pago
    vuelto = procesar_pago(total_neto)
    print(f"✅ Vuelto: ${vuelto:.2f}")
    
    # Determinar si pagó con billete grande (> $200)
    pago_real = total_neto + vuelto
    if pago_real > 200:
        clientes_pago_grande += 1
    
    # Actualizar acumuladores
    total_vendido_dia += total_neto
    
    if total_neto > mayor_gasto:
        mayor_gasto = total_neto
        nombre_mayor = nombre
    
    if total_neto < menor_gasto:
        menor_gasto = total_neto
        nombre_menor = nombre

# Mostrar resumen final
print("\n" + "="*50)
print("📊 RESUMEN DEL DÍA")
print("="*50)
print(f"Total vendido: ${total_vendido_dia:.2f}")
print(f"Clientes atendidos: {num_clientes}")
print(f"Clientes que pagaron con billetes > $200: {clientes_pago_grande}")
print(f"💰 Cliente que más gastó: {nombre_mayor} (${mayor_gasto:.2f})")
print(f"💰 Cliente que menos gastó: {nombre_menor} (${menor_gasto:.2f})")
print(f"💰 Ticket promedio: ${total_vendido_dia/num_clientes:.2f}")