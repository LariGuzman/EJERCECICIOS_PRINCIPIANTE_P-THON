from datetime import datetime
def calcular_dias_vividos (fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime (fecha_nacimiento, "%Y-%m-%d")
    diferencia = fecha_actual-fecha_nacimiento
    dias_vividos = diferencia.days
    return dias_vividos
fecha_nacimiento = input ("Ingrese su fecha de nacimiento (Formato: AAAA-MM-DD):")
dias_vividos = calcular_dias_vividos (fecha_nacimiento)
print ("Has vivido", dias_vividos, "días.")
