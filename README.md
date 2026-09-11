# Tienda de Ropa IT

Trabajo Integrador II — Python Avanzado (Opción 3: Tienda de Ropa)

Sistema de consola para la gestión de pedidos de un local de ropa. Permite registrar ventas por cantidad de producto, calcular el total con descuento opcional, procesar el pago y el vuelto, y dejar constancia de la actividad del turno en un archivo de registro.

## Grupo

Grupo 3 — Python Avanzado, Centro Regional Universitario de Ituzaingó

Integrantes:
- Arispe Gabriel
- López Cristian
- Loza Valentina
- Lucero Germán
- Zárate Elías

## Menú de productos

| Producto  | Precio |
|-----------|--------|
| Remera    | $10    |
| Pantalón  | $20    |
| Buzo      | $25    |
| Gorra     | $8     |


## Flujo del programa

1. **Inicio de sesión del encargad@**
   Al iniciar, el sistema solicita el nombre de quien está a cargo del turno y lo registra en `registro.txt`.

2. **Menú principal**
   ```
   1 - Ingreso nuevo pedido
   2 - Cambio de turno
   3 - Apagar sistema
   ```

3. **Nuevo pedido (opción 1)**
   - Se solicita el nombre del cliente.
   - Se cargan productos y cantidades (opción `0` para finalizar la carga).
   - Se calcula el subtotal.
   - Se consulta si corresponde aplicar un descuento del 10% (opcional).
   - Se solicita el pago y se calcula el vuelto; no se avanza si el monto no alcanza.
   - Se solicita confirmación final (`Y/N`). Si no se confirma, el pedido se descarta y no se guarda.
   - Si se confirma, la venta queda registrada en `registro.txt`.

4. **Cambio de turno (opción 2)**
   Cierra el turno del encargad@ actual, deja constancia en `registro.txt` del total recaudado, y solicita el nombre de un nuevo encargad@ sin apagar el sistema.

5. **Apagar sistema (opción 3)**
   Cierra el turno de la misma manera que la opción 2 y finaliza la ejecución del programa.

## Archivo generado: `registro.txt`

El historial de actividad se guarda en un único archivo, en modo append (no se sobrescribe ni se borra el contenido previo). Contiene tres tipos de líneas:

| Prefijo | Momento en que se genera            | Ejemplo |
|---------|--------------------------------------|---------|
| `IN`    | Al iniciar sesión un encargad@        | `IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo` |
| `VENTA` | Al confirmar un pedido                | `VENTA Sat Oct 23 10:20:00 2021 Cliente Juan Remera:1 Pantalon:1 Buzo:0 Gorra:2 Total:$15` |
| `OUT`   | Al cerrar turno o apagar el sistema   | `OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $46` |

Cada cierre de turno se separa del siguiente mediante una línea de 50 numerales (`#`):

```
IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo
VENTA Sat Oct 23 10:20:00 2021 Cliente Juan Remera:1 Pantalon:1 Buzo:0 Gorra:2 Total:$15
OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $46
##################################################
IN Sat Oct 23 11:41:20 2021 Encargad@ Horacio
```

## Funcionalidades implementadas

- Mensaje de bienvenida e ingreso del encargad@
- Menú principal (nuevo pedido / cambio de turno / apagar sistema)
- Carga de pedido por cantidades de producto
- Cálculo de total y vuelto
- Descuento opcional del 10%
- Confirmación de pedido (Y/N) previa al guardado
- Registro persistente de ingresos, ventas y egresos en `registro.txt`
- Manejo de excepciones: el sistema no se interrumpe ante entradas inválidas ni errores inesperados