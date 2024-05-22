while True:
    entrada = input("Introduce un numero entero: ")
    if entrada.isdigit():
        numero = int(entrada)
        print(f"El numero entrero es {numero}")
        break
    else:
        print("El numero no es entero")