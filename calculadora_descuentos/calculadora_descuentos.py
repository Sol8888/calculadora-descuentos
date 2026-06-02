# ============================================================
# CLASE PRINCIPAL: CalculadoraDescuentos
# ETAPA ACT DEL CICLO PDCA - REFACTORIZACIÓN
# ============================================================

class CalculadoraDescuentos:

    def _validar_positivo(self, valor, nombre_variable):
        """Método privado para validar que las entradas sean numéricas y positivas."""
        if not isinstance(valor, (int, float)):
            raise TypeError(f"{nombre_variable} debe ser un valor numérico.")
        if valor < 0:
            raise ValueError(f"{nombre_variable} no puede ser negativo.")

    # Ciclo 1 - Refactorizado
    def aplicar_descuento_porcentaje(self, monto, porcentaje=10):
        self._validar_positivo(monto, "El monto")
        self._validar_positivo(porcentaje, "El porcentaje")
        
        if porcentaje > 100:
            raise ValueError("El porcentaje de descuento no puede ser mayor a 100.")
            
        descuento = monto * (porcentaje / 100)
        return monto - descuento

    # Ciclo 2 - Refactorizado
    def aplicar_descuento_fijo(self, monto, descuento):
        self._validar_positivo(monto, "El monto")
        self._validar_positivo(descuento, "El descuento fijo")
        
        if descuento > monto:
            raise ValueError("El descuento fijo no puede ser mayor al precio original.")
            
        return monto - descuento
    
    # Ciclo 3 - Refactorizado (Aplicando DRY - Don't Repeat Yourself)
    def aplicar_descuento_acumulado(self, monto, porcentaje, descuento):
        # Reutilizamos los métodos anteriores en lugar de reescribir la lógica matemática
        subtotal = self.aplicar_descuento_porcentaje(monto, porcentaje)
        precio_final = self.aplicar_descuento_fijo(subtotal, descuento)
        
        return precio_final