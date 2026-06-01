# ============================================================
# PRUEBA UNITARIA - ESTUDIANTE 1
# ETAPA PLAN DEL CICLO PDCA
# ============================================================
# En esta etapa definimos el comportamiento esperado antes
# de implementar la lógica de la calculadora.
#
# Objetivo:
# Comprobar que un monto de $100 quede en $90 después de
# aplicar automáticamente un descuento fijo del 10%.
# ============================================================

import unittest

# Importar la clase que posteriormente contendrá la funcionalidad.
from calculadora_descuentos import CalculadoraDescuentos


class TestCalculadoraDescuentos(unittest.TestCase):

    def test_descuento_porcentual_del_diez_por_ciento(self):
        """
        Verifica que un monto de $100 quede en $90
        después de aplicar un descuento automático del 10%.
        """

        # Arrange: preparar los datos de entrada y el resultado esperado.
        calculadora = CalculadoraDescuentos()
        monto = 100
        resultado_esperado = 90

        # Act: ejecutar el método que queremos probar.
        resultado_obtenido = (
            calculadora.aplicar_descuento_porcentaje(monto)
        )

        # Mostrar claramente los valores usados durante la prueba.
        print("\n--- PRUEBA DEL ESTUDIANTE 1 ---")
        print(f"Monto original: ${monto}")
        print("Descuento aplicado: 10%")
        print(f"Resultado esperado: ${resultado_esperado}")
        print(f"Resultado obtenido: ${resultado_obtenido}")

        # Assert: comprobar si el resultado es el esperado.
        self.assertEqual(resultado_obtenido, resultado_esperado)


# Permite ejecutar la prueba desde la terminal.
if __name__ == "__main__":
    unittest.main(verbosity=2)