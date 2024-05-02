print ("Para crear una escalera invertida con asteriscos (*)")
num_lado = int (input("Ingrese el número asteristicos para deterrminar el tamaño del lado del cuadrado"))
for i in range ( 1, num_lado + 1):
    for j in range ( 1, num_lado + 1):
        if i == 1 or j>i:
            print ("* ", end=" ")
        else:
            print ("  ", end = " ")
    print ()
    