# 👕 Tienda de Ropa IT

Trabajo Integrador II – Python Avanzado (Opción 3: Tienda de Ropa)

Sistema de consola para gestionar los pedidos de un local de ropa: permite registrar ventas por cantidad de producto, calcular el total con descuento opcional, procesar el pago y el vuelto, y dejar un registro completo de la actividad del turno en un archivo de texto.

## 👥 Grupo

Grupo 3

**Integrantes:**
- Arispe Gabriel
- Cardozo Camila
- López Cristian
- Loza Valentina
- Lucero Germán
- Zárate Elías

## 📋 Menú de productos

| Producto  | Precio |
|-----------|--------|
| Remera    | $10    |
| Pantalón  | $20    |
| Buzo      | $25    |
| Gorra     | $8     |

## ⚙️ Requisitos

- Python 3.10 o superior
- No requiere librerías externas (solo usa el módulo `time`, incluido en Python)

## ▶️ Cómo ejecutarlo

```bash
python tienda-de-ropa.py
```

## 🧭 Flujo del programa

1. **Inicio de sesión del encargad@**
   Al arrancar, el sistema pide el nombre de quien está a cargo del turno y lo registra automáticamente en `registro.txt`.

2. **Menú principal**
   ```
   1 - Ingreso nuevo pedido
   2 - Cambio de turno
   3 - Apagar sistema
   ```

3. **Nuevo pedido (opción 1)**
   - Se solicita el nombre del cliente.
   - Se eligen productos y cantidades (opción `0` para finalizar la carga).
   - Se calcula el subtotal.
   - Se pregunta si se aplica un **descuento del 10%** (opcional).
   - Se solicita el pago y se calcula el vuelto (no deja continuar si el monto no alcanza).
   - Se pide confirmación final (`Y/N`). Si no se confirma, el pedido se descarta y no se guarda nada.
   - Si se confirma, la venta queda asentada en `registro.txt`.

4. **Cambio de turno (opción 2)**
   Cierra el turno del encargad@ actual, deja constancia en `registro.txt` del total recaudado, y vuelve a pedir el nombre de un nuevo encargad@ sin apagar el sistema.

5. **Apagar sistema (opción 3)**
   Cierra el turno de la misma manera que la opción 2, pero además termina la ejecución del programa.

## 🗂️ Archivo generado: `registro.txt`

Todo el historial de actividad se guarda en un único archivo, en modo *append* (nunca se sobrescribe ni se borra lo anterior). Contiene tres tipos de líneas:

| Prefijo | Cuándo se genera | Ejemplo |
|---------|-------------------|---------|
| `IN`    | Al iniciar sesión un encargad@ | `IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo` |
| `VENTA` | Al confirmar un pedido | `VENTA Sat Oct 23 10:20:00 2021 Cliente Juan Remera:1 Pantalon:1 Buzo:0 Gorra:2 Total:$15` |
| `OUT`   | Al cerrar turno o apagar el sistema | `OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $46` |

Cada cierre de turno se separa del siguiente con una línea de 50 numerales (`#`), a modo de divisor visual:

```
IN Sat Oct 23 10:18:18 2021 Encargad@ Gerardo
VENTA Sat Oct 23 10:20:00 2021 Cliente Juan Remera:1 Pantalon:1 Buzo:0 Gorra:2 Total:$15
OUT Sat Oct 23 11:39:15 2021 Encargad@ Gerardo $46
##################################################
IN Sat Oct 23 11:41:20 2021 Encargad@ Horacio
```

## ✅ Funcionalidades implementadas

- [x] Mensaje de bienvenida e ingreso del encargad@
- [x] Menú principal (nuevo pedido / cambio de turno / apagar sistema)
- [x] Carga de pedido por cantidades de producto
- [x] Cálculo de total y vuelto
- [x] Descuento opcional del 10%
- [x] Confirmación de pedido (Y/N) antes de guardar
- [x] Registro persistente de ingresos, ventas y egresos en `registro.txt`
- [x] Manejo de excepciones: el sistema no se detiene ante entradas inválidas ni errores inesperados