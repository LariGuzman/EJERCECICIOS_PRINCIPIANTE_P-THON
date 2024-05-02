conteo=0
suma=0
Num_mayor=0
Num_menor=0
Numero_ingresado= float (input("Ingresa un número. Teclea 0 para finalizar"))

while Numero_ingresado != 0:
    conteo = conteo + 1
    suma = suma + Numero_ingresado
    Promedio = suma/conteo
    if conteo ==1 or Numero_ingresado < Num_menor:
        Num_menor = Numero_ingresado
    if Numero_ingresado > Num_mayor:
        Num_mayor=Numero_ingresado
    Numero_ingresado = float (input("Ingresa un número. Teclea 0 para finalizar"))
print("La media de los números ingresados es: ", Promedio)
print ("El mínimo de los números ingresados es: ",  Num_menor)
print ("El máximo de los números ingresados es: ",  Num_mayor)
                     