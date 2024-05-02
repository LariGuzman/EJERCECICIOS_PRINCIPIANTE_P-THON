def incremento_salarial(salario_actual):
    if salario_actual >= 15000:
        calculo_incremento = salario_actual*1.15
    else:
        calculo_incremento = salario_actual*1.20
    return calculo_incremento
salario_actual = float (input ("Ingrese el monto de su salario mensual actual:"))
salario_incrementado = incremento_salarial(salario_actual)


print ("Su salario actual actualizado es de $", salario_incrementado)