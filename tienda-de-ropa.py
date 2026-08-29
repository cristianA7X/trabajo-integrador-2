"""
OPCIÓN 3 –Tienda de Ropa 👕

Un local de ropa quiere registrar ventas.
• 📋 Productos:
• Remera → $10
• Pantalón → $20
• Buzo → $25
• Gorra → $8

• 💡 Adaptación
• Igual que hamburguesería:
• Pedido por cantidades
• Cálculo total
• Pago y vuelto
• Confirmación
• Guardado en archivo
• Podés sumar:
Descuento opcional (por ejemplo 10%)
"""

import time

menu = {
    "1": {"nombre": "Remera", "precio": 10},
    "2": {"nombre": "Pantalón", "precio": 20},
    "3": {"nombre": "Buzo", "precio": 25},
    "4": {"nombre": "Gorra", "precio": 8},
}

def pedir_entero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero válido.")
            continue

        if num >= 0:
            return num
        else:
            print("Debe ingresar un número mayor o igual a 0.")

def registroEntrada(encargado):
    fecha = time.asctime()
    with open("registro.txt", "a") as f:
        f.write(f"IN {fecha} Encargad@ {encargado}\n")
    print(f"\n[SISTEMA] Registro de entrada completado para: {encargado}")

def registroSalida(encargado, total):
    fecha = time.asctime()
    with open("registro.txt", "a") as f:
        f.write(f"OUT {fecha} Encargad@ {encargado} ${total}\n")
        f.write("#" * 50 + "\n")

def prtProductos():
    print("\nProductos disponibles:")
    for clave in menu:
        producto = menu[clave]
        print(f"{clave} - {producto['nombre']} (${producto['precio']})")

def nuevo_pedido(total_turno):
    cliente = input("\nIngrese nombre del cliente: ")

    cantidades = {}
    prtProductos()

    while True:
        opcion = input("\nElija un producto (0 para finalizar el pedido): ")

        if opcion == "0":
            break
        else:
            producto = menu.get(opcion)
            if producto:
                cantidad = pedir_entero(f"Cantidad de {producto['nombre']}: ")
                cantidades[opcion] = cantidades.get(opcion, 0) + cantidad
            else:
                print("Opción inválida. Intente de nuevo.")

    total = 0
    for clave in cantidades:
        cantidad = cantidades[clave]
        total += cantidad * menu[clave]["precio"]

    if total == 0:
        print("No se seleccionó ningún producto. Pedido cancelado.")
        return total_turno

    print(f"\nSubtotal ${total}")

    while True:
        aplicar_descuento = input("¿Aplicar descuento del 10%? Y/N : ").strip().upper()
        if aplicar_descuento in ("Y", "N"):
            break
        else:
            print("Respuesta inválida. Ingrese Y o N.")

    if aplicar_descuento == "Y":
        total = round(total * 0.9)
        print(f"Descuento aplicado. Total ${total}")
    else:
        print(f"Total ${total}")

    while True:
        pago = pedir_entero("Abona con $ ")
        if pago >= total:
            break
        else:
            print(f"El monto no alcanza. Faltan ${total - pago}. Intente de nuevo.")

    vuelto = pago - total
    print(f"Vuelto ${vuelto}")

    while True:
        confirma = input("\n¿Confirma pedido? Y/N : ").strip().upper()
        if confirma in ("Y", "N"):
            break
        else:
            print("Respuesta inválida. Ingrese Y o N.")

    if confirma == "N":
        print("Pedido cancelado.")
        return total_turno

    print(f"Pedido registrado para {cliente}. Total venta: ${total}")

    fecha = time.asctime()
    cant_remera = cantidades.get("1", 0)
    cant_pantalon = cantidades.get("2", 0)
    cant_buzo = cantidades.get("3", 0)
    cant_gorra = cantidades.get("4", 0)

    with open("registro.txt", "a") as f:
        f.write(
            f"VENTA {fecha} Cliente {cliente} "
            f"Remera:{cant_remera} Pantalon:{cant_pantalon} Buzo:{cant_buzo} Gorra:{cant_gorra} "
            f"Total:${total}\n"
        )

    return total_turno + total

def prtMenu(encargado):
    print("\nTienda de Ropa IT")
    print(f"Encargad@ -> {encargado}")
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)\n")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")

def main():
    sistema_activo = True

    while sistema_activo:
        print("\n--- Bienvenido a la Tienda de Ropa IT ---")
        encargado = input("Ingrese el nombre del encargado: ")
        registroEntrada(encargado)

        totalTurno = 0
        en_turno = True

        while en_turno:
            prtMenu(encargado)
            opcion = input("Seleccione una opcion: ")

            try:
                if opcion == "1":
                    totalTurno = nuevo_pedido(totalTurno)
                    print(f"Recaudación actual del turno: ${totalTurno}")
                elif opcion == "2":
                    print(f"\nCerrando turno de {encargado}. Total recaudado: ${totalTurno}")
                    registroSalida(encargado, totalTurno)
                    en_turno = False
                elif opcion == "3":
                    print(f"\nCerrando turno de {encargado}. Total recaudado: ${totalTurno}")
                    registroSalida(encargado, totalTurno)
                    print("Apagando sistema")
                    en_turno = False
                    sistema_activo = False
                else:
                    print("Opción invalida.")
            except Exception as error:
                print(f"\n[SISTEMA] Ocurrió un error inesperado: {error}")
                print("Continuando con el funcionamiento normal del sistema...")

main()