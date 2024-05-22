monto = float(input("Ingrese el monto de compra: "))

if monto >= 100:
    descuentp = monto*(float(input("Ingrese el porecntaje de compra: ")))/100
    monto -= descuentp
    print(f"Se aplico un descuento de {descuentp} pesos")
else:
    print("No se aplico descuento")