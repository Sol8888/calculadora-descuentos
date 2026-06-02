# ============================================================
# APLICACIÓN PRINCIPAL
# CALCULADORA DE DESCUENTOS
# ============================================================
# Este programa permite ingresar manualmente el precio original
# de un producto.
#
# El sistema aplica automáticamente un descuento fijo del 10%.
# ============================================================

from calculadora_descuentos import CalculadoraDescuentos

calculadora = CalculadoraDescuentos()

print("======================================")
print("      CALCULADORA DE DESCUENTOS")
print("======================================")

try:
    entrada = input("\nIngrese el precio original del producto: $")
    monto = float(entrada) # Esto lanzará ValueError si ingresan letras

    # Por defecto aplicará el 10%
    precio_final = calculadora.aplicar_descuento_porcentaje(monto)

    print("\n========== RESULTADO ==========")
    print(f"Precio original: ${monto:.2f}")
    print("Descuento aplicado: 10%")
    print(f"Precio final: ${precio_final:.2f}")

except ValueError as ve:
    # Captura errores de validación de negocio (negativos) y errores de casteo (letras a float)
    print(f"\n[ERROR]: Entrada inválida. {ve}")
except TypeError as te:
    print(f"\n[ERROR DE SISTEMA]: {te}")
except Exception as e:
    print(f"\n[ERROR INESPERADO]: Ha ocurrido un problema - {e}")