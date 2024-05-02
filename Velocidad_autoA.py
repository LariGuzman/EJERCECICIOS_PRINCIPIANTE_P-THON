print ("Calcule el tiempo que toma en recorrer un auto la distancia ingresada")
def velocidad_auto (distancia,velocidad):
    tiempo_decimal = distancia/velocidad
    return tiempo_decimal
distancia = float (input("Ingrese la distancia que debe recorrerse (en kilómetros):"))
velocidad= float (input ("Introduzca el número de kilómetros que recorre un auto en una hora:"))
tiempo_decimal = velocidad_auto (distancia,velocidad)
tiempo_horas = tiempo_decimal // 1
tiempo_minutos = (tiempo_decimal-tiempo_horas) *60

if tiempo_horas == 1:
    print ("El tiempo que tardará en recorrer ", distancia, "km  es de 1 hora")
elif tiempo_horas == tiempo_decimal:
    print ("El tiempo que tardará en recorrer ", distancia, "km  es de ", tiempo_horas, "horas")
else:
    print ("El tiempo que tardará en recorrer ", distancia, "km  es de ", tiempo_horas, "horas y ", int(tiempo_minutos), "minutos" )

