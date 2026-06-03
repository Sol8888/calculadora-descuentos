# ============================================================
# CLASE PRINCIPAL: CalculadoraDescuentos
# ETAPA ACT DEL CICLO PDCA - REFACTORIZACIÓN
# ============================================================

class CalculadoraDescuentos:

    def aplicar_descuento_porcentaje(self, monto, porcentaje):
        """
        Ciclo 1: Aplica un descuento porcentual dinámico.
        Firma equivalente: aplicarDescuentoPorcentaje(double monto, double porcentaje)
        """
        if monto < 0 or porcentaje < 0:
            raise ValueError("El monto y el porcentaje no pueden ser negativos.")
        if porcentaje > 100:
            raise ValueError("El porcentaje no puede ser mayor al 100%.")
            
        descuento = monto * (porcentaje / 100)
        return monto - descuento

    def aplicar_descuento_fijo(self, monto, descuento):
        """
        Ciclo 2: Aplica un descuento por cantidad fija.
        Firma equivalente: aplicarDescuentoFijo(double monto, double descuento)
        """
        if monto < 0 or descuento < 0:
            raise ValueError("El monto y el descuento fijo no pueden ser negativos.")
        if descuento > monto:
            raise ValueError("El descuento fijo no puede ser mayor al monto original.")
            
        return monto - descuento
    
    def aplicar_descuento_acumulado(self, monto, porcentaje, descuento):
        """
        Ciclo 3: Aplica primero el descuento porcentual y luego el fijo.
        Reutiliza los métodos de los ciclos 1 y 2 (Principio DRY).
        """
        subtotal = self.aplicar_descuento_porcentaje(monto, porcentaje)
        precio_final = self.aplicar_descuento_fijo(subtotal, descuento)
        return precio_final

    def verificar_precio_final(self, monto_original, precio_final):
        """
        Ciclo 4: Método explícito para verificar la validez del precio final 
        después de aplicar las transformaciones de descuento.
        Returns:
            bool: True si el precio final cumple con las reglas de negocio.
        """
        # Regla 1: El precio final no puede ser negativo.
        if precio_final < 0:
            raise ValueError("Verificación Fallida: El precio final no puede ser menor a cero.")
        
        # Regla 2: El precio final no puede ser superior al monto original.
        if precio_final > monto_original:
            raise ValueError("Verificación Fallida: El precio final no puede superar al monto original.")
            
        return True