f = 1
print ("Escribe el número del cual deseas conocer su factorial:")
n= float(input())
for i in range (1,int(n)+1):
    f *= i
print ("El factorial de ", n, "es", f)