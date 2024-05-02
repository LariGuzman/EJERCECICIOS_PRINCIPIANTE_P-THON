print("Escribe una palabra para verificar si es un PALÍNDROMO")
palabra = input("Ingrese la palabra: ")
largopalabra = len(palabra)
reves = ""

for i in range(largopalabra, 0, -1):
    reves += palabra[i - 1]

if reves == palabra:
    print("La palabra", palabra, "es PALÍNDROMO")
else:
    print("La palabra", palabra, "NO es PALÍNDROMO")
