clave_correcta = "padawan"
intentos_maximos = 3
for intento in range (1,intentos_maximos+1):
    clave_ingresada = input("Ingrese la clave: ")
    if clave_ingresada == clave_correcta:
        print ("Ingreso exitoso")
        break
    else:
        print ("Clave incorrecta. Intento {} de {}". format(intento, intentos_maximos))
if intento == intentos_maximos:
    print ("Número de intentos superado. Vuelva más tarde")