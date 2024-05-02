alumnos_inscritos = float(input("Ingrese el número de niños inscritos en el curso: "))
alumnas_inscritas = float(input ("Ingrese el número de niñas inscritos en el curso: "))
alumnos_totales = alumnos_inscritos+alumnas_inscritas
porcentaje_niños = (alumnos_inscritos*100)/alumnos_totales
porcentaje_niñas = (alumnas_inscritas*100)/alumnos_totales
print ("El porcentaje de niños en el curso es", porcentaje_niños, "%")
print ("El porcentaje de niñas en el curso es", porcentaje_niñas, "%")