numeros = []
for i in range(5):
    numero = float (input(f"Ingrese un número:"))
    numeros.append(numero)
numeros_ordenados = sorted(numeros)
print ("Los números ordenados de manor a mayor son:")
for numero in numeros_ordenados:
    print(numero)