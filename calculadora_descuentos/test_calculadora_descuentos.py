# ============================================================
# PRUEBAS UNITARIAS - ESTUDIANTES 1 Y 2
# ETAPA PLAN DEL CICLO PDCA — CICLO 1 Y CICLO 2
# ============================================================
# CICLO 1 (Estudiante 1):
#   Comprobar que un monto de $100 quede en $90 después de
#   aplicar automáticamente un descuento porcentual del 10%.
#
# CICLO 2 (Estudiante 2):
#   Comprobar que al aplicar un descuento fijo en dólares
#   el precio final sea el resultado de restar dicho monto.
#   Ejemplo: $100 con descuento de $5 debe quedar en $95.
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

    def test_descuento_porcentual_para_cuatrocientos_dolares(self):
        """
        PRUEBA ADICIONAL - ETAPA ACT

        Objetivo:
            Verificar que el método también funcione con otro monto.

        Caso esperado:
            Si el precio original es $400 y se aplica un descuento
            automático del 10%, el precio final debe ser $360.
        """

        # Arrange: preparar los datos de entrada.
        calculadora = CalculadoraDescuentos()
        monto = 400
        resultado_esperado = 360

        # Act: ejecutar el método que aplica el descuento.
        resultado_obtenido = (
            calculadora.aplicar_descuento_porcentaje(monto)
        )

        # Mostrar los valores utilizados durante la prueba.
        print("\n--- PRUEBA ADICIONAL DEL ESTUDIANTE 1 ---")
        print(f"Monto original: ${monto}")
        print("Descuento aplicado: 10%")
        print(f"Resultado esperado: ${resultado_esperado}")
        print(f"Resultado obtenido: ${resultado_obtenido}")

        # Assert: comprobar que el resultado sea correcto.
        self.assertEqual(resultado_obtenido, resultado_esperado)
        
        #CICLO 2
    def test_descuento_fijo_de_cinco_dolares(self):
        """
            Verificar que al aplicar un descuento fijo de $5
            a un precio de $100, el resultado sea $95.
        """

        # Arrange
        calculadora = CalculadoraDescuentos()
        monto = 100
        descuento = 5
        resultado_esperado = 95

        # Act
        resultado_obtenido = calculadora.aplicar_descuento_fijo(
            monto, descuento
        )

        # Mostrar valores
        print("\n--- PRUEBA DEL ESTUDIANTE 2 ---")
        print(f"Monto original:     ${monto}")
        print(f"Descuento fijo:     ${descuento}")
        print(f"Resultado esperado: ${resultado_esperado}")
        print(f"Resultado obtenido: ${resultado_obtenido}")

        # Assert
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_descuento_fijo_para_doscientos_dolares(self):
        """
            Si el precio original es $200 y se aplica un descuento
            fijo de $30, el precio final debe ser $170.
        """

        # Arrange
        calculadora = CalculadoraDescuentos()
        monto = 200
        descuento = 30
        resultado_esperado = 170

        # Act
        resultado_obtenido = calculadora.aplicar_descuento_fijo(
            monto, descuento
        )

        # Mostrar valores
        print("\n--- PRUEBA ADICIONAL DEL ESTUDIANTE 2 ---")
        print(f"Monto original:     ${monto}")
        print(f"Descuento fijo:     ${descuento}")
        print(f"Resultado esperado: ${resultado_esperado}")
        print(f"Resultado obtenido: ${resultado_obtenido}")

        # Assert
        self.assertEqual(resultado_obtenido, resultado_esperado)

# Permite ejecutar la prueba desde la terminal.
if __name__ == "__main__":
    unittest.main(verbosity=2)
