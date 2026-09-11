# Tienda de Ropa IT


Sistema de consola para gestionar pedidos de un local de ropa: carga de productos por cantidad, cálculo de total con descuento opcional, pago, vuelto y registro de la actividad del turno.

## Grupo

Grupo 3

- Arispe Gabriel
- López Cristian
- Loza Valentina
- Lucero Germán
- Zárate Elías

## Productos

- Remera: $10
- Pantalón: $20
- Buzo: $25
- Gorra: $8

## Uso

1. Se ingresa el nombre del encargad@ del turno.
2. Menú principal: nuevo pedido, cambio de turno o apagar sistema.
3. En un pedido: nombre del cliente, productos y cantidades, descuento opcional del 10%, pago, vuelto y confirmación (Y/N). Solo se guarda si se confirma.
4. Al cambiar de turno o apagar el sistema se registra el total recaudado.

## registro.txt

Toda la actividad se guarda en un único archivo, en modo append. Tres tipos de línea:

```
IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo
VENTA Sat Oct 23 10:20:00 2021 Cliente Juan Remera:1 Pantalon:1 Buzo:0 Gorra:2 Total:$15
OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $46
##################################################
```
