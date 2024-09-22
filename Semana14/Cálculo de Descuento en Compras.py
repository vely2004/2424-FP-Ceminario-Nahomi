def calcular_descuento(monto_sin_iva, porcentaje_descuento=30):
    # Calcular el descuento
    descuento = monto_sin_iva * (porcentaje_descuento / 100)
    monto_final_sin_iva = monto_sin_iva - descuento

    # Calcular el IVA (15%)
    iva = monto_final_sin_iva * 0.15

    # Monto total con IVA incluido
    monto_total = monto_final_sin_iva + iva

    return descuento, monto_final_sin_iva, iva, monto_total


# Solicitar el gasto en compras adquirido
if __name__ == '__main__':
        # Primera compra
        monto_final_sin_iva1 = float(input("Ingresa el total de tu primera compra sin IVA: "))

        # Primera llamada a la función
        descuento1, monto_final_sin_iva1, iva1, monto_total1 = calcular_descuento(monto_final_sin_iva1)

        # Resultados de la primera llamada
        print("\nResultados de la primera compra:")
        print(f"Descuento aplicado: ${descuento1:.2f}")
        print(f"Monto final sin IVA: ${monto_final_sin_iva1:.2f}")
        print(f"IVA (15%): ${iva1:.2f}")
        print(f"Monto total con IVA: ${monto_total1:.2f}")

        # Segunda compra
        monto_final_sin_iva2 = float(input("\nIngresa el total de tu segunda compra sin IVA: "))

        # Segunda llamada a la función
        descuento2, monto_final_sin_iva2, iva2, monto_total2 = calcular_descuento(monto_final_sin_iva2)

        # Resultados de la segunda llamada
        print("\nResultados de la segunda compra:")
        print(f"Descuento aplicado: ${descuento2:.2f}")
        print(f"Monto final sin IVA: ${monto_final_sin_iva2:.2f}")
        print(f"IVA (15%): ${iva2:.2f}")
        print(f"Monto total con IVA: ${monto_total2:.2f}")