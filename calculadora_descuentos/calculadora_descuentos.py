# ============================================================
# CLASE PRINCIPAL: CalculadoraDescuentos
# ETAPA CHECK DEL CICLO PDCA
# ============================================================
# En esta etapa corregimos la implementación para que la prueba
# unitaria pase correctamente.
#
# La funcionalidad debe aplicar automáticamente un descuento
# fijo del 10% al monto ingresado.
# ============================================================


class CalculadoraDescuentos:

    def aplicar_descuento_porcentaje(self, monto):
        """
        Aplica automáticamente un descuento fijo del 10%.

        Parámetro:
            monto: precio original del producto.

        Retorna:
            precio final después de aplicar el descuento.

        Ejemplo:
            monto = 100
            descuento = 10
            precio final = 90
        """

        # El porcentaje se mantiene fijo porque corresponde
        # a la primera funcionalidad del ejercicio.
        porcentaje = 10

        # Calcular cuánto dinero representa el 10% del monto.
        descuento = monto * porcentaje / 100

        # Restar el descuento al precio original.
        precio_final = monto - descuento

        # Retornar el precio final calculado.
        return precio_final
    # Ciclo 2
    def aplicar_descuento_fijo(self, monto, descuento):
        precio_final = monto - descuento
        return precio_final