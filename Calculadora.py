def calculadora (numero1, numero2, operacion):
    if operacion == 'suma':
        return numero1+numero2
    elif operacion== 'resta':
        return numero1-numero2
    elif operacion== 'multiplicación':
        return numero1*numero2
    elif operacion=='división':
        return numero1/numero2
        if numero2 != 0:
            return numero1/numero2
        else:
            return "Error. división entre 0"
    else: 
        return "Error, ingrese los datos adecuadamente"
numero1= float (input ("Ingrese el primer número:"))
numero2= float (input ("Ingrese el segundo número:"))
operacion= input ("Ingrese la operación que desea realizar: (suma, resta, multiplicación o división)")

resultado=calculadora(numero1, numero2, operacion)
print ("el resultado de la operación seleccionada es: ", resultado)
  