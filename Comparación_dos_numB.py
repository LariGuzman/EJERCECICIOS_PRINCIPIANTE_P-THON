def encontrar_mayor (numero1, numero2):
    if numero1> numero2:
        return numero1
    elif numero2> numero1:
        return numero2
    else:
        return "Ambos números son iguales"
numero1= float(input ("Ingrese el primer número:"))
numero2= float(input ("Ingrese el primer número:"))

mayor = encontrar_mayor(numero1, numero2)
print ("el número mayor es", mayor)