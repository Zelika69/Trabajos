import time
año = int(input("Ingrese el año: "))
if (año % 4 == 0 and año % 400 != 0) or (año % 400 ==0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} No es un año bisiesto")