while True:
    password = input("Introduce una contraseña maximo de 8 digitos: ")
    if len(password) > 8:
        print("Contraseña segura")
        break
    else:
        print("contraseña no segura")