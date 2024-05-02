print("Para crear una escalera invertida con asteriscos (*)")
Num_lado = int(input("Ingrese el número de asteriscos para determinar el tamaño del lado del cuadrado: "))

for i in range(1, Num_lado + 1):
    for j in range(1, Num_lado + 1):
        if i == 1 or j >= i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()  # Cambiar de línea después de imprimir cada fila
