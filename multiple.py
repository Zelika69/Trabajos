from datetime import datetime
hora_actual = datetime.now()
edad = int(input("Ingresa la Edad: "))

hora = hora_actual.strftime("%H:%M")
if edad <= 5:print("Los niños viajan gratis")
elif edad >= 65:
    if (hora >= "07:00" and hora <= "09:00") or (hora >= "17:00" and hora <= "19:00"): print("El pasaje es de $100 pesos hora pico y no se aplico descuento por ser mayor a 65 años")
    else:print("El pasaje es de $75 aplicando un descuento del 35% por ser mayor a 65 años")
elif (hora >= "07:00" and hora <= "09:00") or (hora >= "17:00" and hora <= "19:00") and edad>5: print("El pasaje es $140 por ser usuario normal y aplicando el monto extra por las horas pico")
else:print("El pasaje es de $120 por ser usuario normal")
print(f"Hora de compra: {hora}")