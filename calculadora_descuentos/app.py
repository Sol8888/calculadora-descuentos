from calculadora_descuentos import CalculadoraDescuentos

calculadora = CalculadoraDescuentos()

print("======================================")
print("      CALCULADORA DE DESCUENTOS")
print("======================================")

try:
    monto = float(input("\nIngrese el precio original del producto: $"))
    porcentaje_descuento = 10.0  # Parametrizado explícitamente

    # Ejecución del cálculo (Ciclo 1 refactorizado)
    precio_final = calculadora.aplicar_descuento_porcentaje(monto, porcentaje_descuento)

    # Compuerta de verificación obligatoria (Ciclo 4)
    if calculadora.verificar_precio_final(monto, precio_final):
        print("\n========== RESULTADO VERIFICADO ==========")
        print(f"Precio original: ${monto:.2f}")
        print(f"Descuento aplicado: {porcentaje_descuento}%")
        print(f"Precio final: ${precio_final:.2f}")

except ValueError as e:
    print(f"\n[ERROR DE VALIDACIÓN]: {e}")
except Exception as e:
    print(f"\n[ERROR INESPERADO]: {e}")