from datetime import datetime
hora_actual = datetime.now()
print("La hora actual es: ", hora_actual.strftime("%H:%M:%S"))

hora = hora_actual.strftime("%H:%M")

if hora < "12:00":
    print("Se hizo antes de las 12:00")
else:
    print("Se hizo después de las 12:00")