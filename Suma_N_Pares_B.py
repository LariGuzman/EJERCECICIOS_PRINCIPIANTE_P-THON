"ALERTA!!!!! ESTA PROPUESTA DE CHAT GPT NO FUNCIONA PARA LO SOLICITADO"
N = int(input("Ingrese un número entero positivo para calcular la suma de los siguientes números pares: "))

suma = 0
numero = N + 1  # Empezamos desde el número siguiente a N

for _ in range(N):  # Repetimos N veces
    suma += numero
    print (suma)
    numero += 2  # Avanzamos al siguiente número par
    print (numero)
print("La suma de los siguientes", N, "números pares después de", N, "es:", suma)
