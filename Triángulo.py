def area_triangulo(base,altura):
    resultado = ((base*altura)/2)
    return resultado  
base = float (input("Ingrese la base del triángulo en cm:"))
altura = float (input("Ingrese la altura del triángulo en cm:"))
area = area_triangulo (base,altura)
print ("El área del triángulo es", area, "cm²)