numero_origen = int(input ("Ingresa un número: "))
suma = 0
for i  in range ( numero_origen + 1, (numero_origen + (numero_origen * 2) + 1)):
    prueba = i/2
    if prueba.is_integer ():
        print (i)
        suma += i
print ("La suma de los", numero_origen, "primeros números pares siguientes al número ingresado es", suma)
