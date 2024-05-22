while True:
    opcion = str(input(''''
    1)Suma
    2)Resta
    3)Multiplicación
    4)División
                       '''))
    var1 = float(input("Ingrese la primera variable: "))
    var2 = float(input("Ingrese la segunda variable: "))
    
    if opcion == 1:
        resultado = var1 + var2
    elif opcion == 2:
        resultado = var1 - var2
    elif opcion == 3:
        resultado = var1 * var2
    elif opcion == 4:
        resultado = var1/var2
    else:
        resultado = var1/var2
            
        