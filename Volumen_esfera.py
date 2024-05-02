#Calcule el volumen de una esfera
import math
# Para poder usar la constante matemática pi y otras funciones matemáticas como math.pi
def calcular_volumen_esfera(radio):
	volumen= (4/3)* math.pi*radio**3
	return volumen
print ("A continuación calcularemos el volumen de una esfera")
radio = float(input("Ingrese el radio de la esfera "))
volumen = calcular_volumen_esfera(radio)
print ("El volumen de la esfera es de:", volumen)
