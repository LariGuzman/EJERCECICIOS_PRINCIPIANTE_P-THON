def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Solicitar la base y la altura al usuario
base = float(input("Ingrese la base del triángulo en cm: "))
altura = float(input("Ingrese la altura del triángulo en cm: "))

# Calcular el área del triángulo utilizando la función
area_triangulo = calcular_area_triangulo(base, altura)

# Imprimir el resultado
print("El área del triángulo es:", area_triangulo, "cm²")