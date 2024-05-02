def incremento_salarial(salario_actual):
    if salario_actual < 15000:
        incremento = salario_actual * 0.20  # Incremento del 20% si el salario es menor a 15000
    else:
        incremento = salario_actual * 0.15  # Incremento del 15% si el salario es mayor o igual a 15000
    return incremento

# Solicitar al usuario que ingrese el salario actual
salario_actual = float(input("Ingrese el monto de su salario mensual actual: "))

# Calcular el incremento salarial utilizando la función incremento_salarial
incremento = incremento_salarial(salario_actual)

# Calcular el nuevo salario sumando el incremento al salario actual
nuevo_salario = salario_actual + incremento

# Imprimir el resultado
print("El incremento salarial es de $", incremento)
print("Su nuevo salario es de $", nuevo_salario)
