# PASO 1: Datos de la cafeteria
print("==========================================")
print("     SISTEMA DE PUNTO DE VENTA (POS)     ")
print("==========================================")

menu = {
    1: ("Café Americano", 35.0),
    2: ("Capuchino", 45.0),
    3: ("Muffin de Arándanos", 30.0),
    4: ("Panini de Jamón y Queso", 65.0)
}

carrito = []
# PASO 2: Ciclo para agregar productos al carrito
comprando = True

while comprando:
    print("\n--- MENÚ DE PRODUCTOS ---")
    for clave, datos in menu.items():
        print(f"[{clave}] {datos[0]} - ${datos[1]}")
    print("[5] Finalizar orden y generar ticket")

    opcion = int(input("\nSeleccione el producto a agregar: "))

    if opcion in [1, 2, 3, 4]:
        producto_elegido = menu[opcion]
        carrito.append(producto_elegido)
        print(f"✔ Agregado a la cuenta: {producto_elegido[0]}")
    elif opcion == 5:
        comprando = False
    else:
        print("❌ Opción no válida. Ingrese un número del menú.")
        
# PASO 3: Generación del comprobante de venta y cobro
print("\n==========================================")
print("             TICKET DE COMPRA             ")
print("==========================================")

subtotal = 0.0
for producto, precio in carrito:
    print(f"• {producto:<25} ${precio:>6.2f}")
    subtotal += precio

print("-" * 42)
print(f"Subtotal:                  ${subtotal:>6.2f}")

# Estrategia de ventas: Descuento por consumo alto
descuento = 0.0
if subtotal >= 100:
    descuento = subtotal * 0.10
    print(f"Descuento Cliente VIP (10%): -${descuento:>6.2f}")

total_final = subtotal - descuento
print(f"TOTAL A PAGAR:             ${total_final:>6.2f}")
print("==========================================")
print("   ¡Gracias por impulsar su negocio! ☕   ")
print("==========================================")