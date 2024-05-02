#Ordene 5 números de menor a mayor
datos = [0] * 5
for i in range(5):
    print ("Ingrese un número")
    datos[i] = float(input())
for i in range (4):
    for j in range (i+1, 5):
        if datos[i]> datos[j]:
            auxiliar = datos[i]
            datos[i] = datos [j]
            datos [j] = auxiliar
print ("Los números ordenados de menor a mayor son:", end= " ")
for i in range (5):
    print(datos [i], end= " ")