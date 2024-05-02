maximo = 0
minimo = 0
suma_numeros = 0
contador_numeros = 0 
numero = float(input("Ingrese un número entero ( o 0 para terminar): "))
while numero != 0:
    if  numero > maximo:
        maximo = numero
    if numero !=0 or numero < minimo:
        minimo = numero
    suma_numeros += numero
    contador_numeros += 1 
    numero = float(input("Ingrese un número entero ( o 0 para terminar):"))
if contador_numeros > 0:
    media = suma_numeros / contador_numeros
    print ("El maximo es:", maximo)
    print ("El mínimo es : ", minimo)
    print ("la media es: ", media)   