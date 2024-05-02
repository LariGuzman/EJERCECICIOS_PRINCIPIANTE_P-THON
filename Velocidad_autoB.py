def calcular_tiempo(velocidad, distancia):
    # Calcula el tiempo requerido para recorrer la distancia dada a la velocidad dada
    tiempo = distancia / velocidad
    return tiempo

# Solicitar al usuario que ingrese la velocidad en km/h y la distancia en km
velocidad = float(input("Ingrese la velocidad del carro (en km/h): "))
distancia = float(input("Ingrese la distancia que debe recorrer el carro (en km): "))

# Calcular el tiempo utilizando la función calcular_tiempo
tiempo_recorrido = calcular_tiempo(velocidad, distancia)

# Imprimir el resultado
print("El tiempo requerido para recorrer la distancia es de", tiempo_recorrido, "horas.")
