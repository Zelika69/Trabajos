edad = int(input("¿Cuantos años tienes?: "))
if edad < 18:
    print("Precio del boleto: $5")
elif edad >= 60:
    print("precio del boleto: $6")
else:
    print("El precio es de $100")