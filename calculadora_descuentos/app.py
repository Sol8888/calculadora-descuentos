# ============================================================
# APLICACIÓN PRINCIPAL
# CALCULADORA DE DESCUENTOS
# ============================================================
# Este programa permite ingresar manualmente el precio original
# de un producto.
#
# El sistema aplica automáticamente un descuento fijo del 10%.
# ============================================================

# Importar la clase principal.
from calculadora_descuentos import CalculadoraDescuentos


# Crear una instancia de la calculadora.
calculadora = CalculadoraDescuentos()

# Mostrar el título del programa.
print("======================================")
print("      CALCULADORA DE DESCUENTOS")
print("======================================")
print("Descuento automático aplicado: 10%")

# Pedir al usuario que ingrese el precio original.
monto = float(
    input("\nIngrese el precio original del producto: $")
)

# Aplicar automáticamente el descuento del 10%.
precio_final = calculadora.aplicar_descuento_porcentaje(monto)

# Mostrar el resultado.
print("\n========== RESULTADO ==========")
print(f"Precio original: ${monto:.2f}")
print("Descuento aplicado: 10%")
print(f"Precio final: ${precio_final:.2f}")