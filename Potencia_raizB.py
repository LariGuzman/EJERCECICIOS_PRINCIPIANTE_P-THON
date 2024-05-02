import math

numero = float(input("Ingrese un número: "))

if numero <= 0:
    print("Error: El número ingresado debe ser mayor que 0.")
else:
    cuadrado = numero ** 2
    raiz_cuadrada = math.sqrt(numero)
    print("Del número", numero, ", su potencia es", cuadrado, "y su raíz cuadrada es", raiz_cuadrada)