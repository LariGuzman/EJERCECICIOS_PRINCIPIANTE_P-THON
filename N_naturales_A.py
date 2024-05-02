suma = 0
Num_Naturales = int(input("Ingrese el número de números naturales de los cuales desea calcular la suma:"))
for i in range (1,Num_Naturales+1):
    suma += i 
print ("La suma de los primeros", Num_Naturales,"es:", suma)