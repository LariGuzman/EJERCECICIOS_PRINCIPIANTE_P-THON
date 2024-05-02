import os
intento = 1
while intento <= 3:
    clave_ingreso = input("Ingrese la contraseña: ")
    if clave_ingreso == "padawan":
        print ("Ingreso exitoso")
        break
    else:
        print (" Clave incorrecta")
        intento += 1
        os.system("cls" if os.name == "nt" else "clear")
        if intento > 3:
            print ("Número de intentos superado, vuelva más tarde")

    