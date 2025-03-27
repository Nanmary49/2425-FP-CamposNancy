def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar sobre un monto total.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función con solo el monto total de la compra
monto1 = 1200  # Ejemplo de monto total
monto_descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - monto_descuento1
print(f"Monto total: ${monto1:.2f}, Descuento: ${monto_descuento1:.2f}, Monto final: ${monto_final1:.2f}")

# Llamada a la función con el monto total y un porcentaje de descuento personalizado
monto2 = 1500  # Otro ejemplo de monto total
porcentaje2 = 15  # Descuento del 15%
monto_descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - monto_descuento2
print(f"Monto total: ${monto2:.2f}, Descuento: ${monto_descuento2:.2f}, Monto final: ${monto_final2:.2f}")