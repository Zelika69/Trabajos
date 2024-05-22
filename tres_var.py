num1 = float(input("Numero uno: "))
num2 = float(input("Numero dos: "))
num3 = float(input("Numero tres: "))
if num1 > num2 and num1 > num3:
    print(f"El mayor es {num1}")
elif num2 > num3:
    print(f"El mayor es {num2}")
elif num1 == (num2 or num3):
    print("Los numeros son iguales")
else:
    print(f"El mayor es {num3}")
    