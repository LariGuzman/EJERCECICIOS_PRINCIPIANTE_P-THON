def si_bisiesto (año_ingresado):
    if año_ingresado%4 == 0:
        if año_ingresado%100 == 0:
            if año_ingresado%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
año_ingresado = float(input("Ingresa un año para verificar si es bisiesto:"))
bisiesto = si_bisiesto (año_ingresado)
if bisiesto == True:
    print ("El año", año_ingresado, "es bisiesto")
if bisiesto == False:
    print ("El año", año_ingresado, "no es bisiesto")