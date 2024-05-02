from datetime import datetime

def dias_faltantes(fecha_actual, fecha_objetivo):
    """Función para calcular los días faltantes entre dos fechas."""
    diferencia = fecha_objetivo - fecha_actual
    return diferencia.days

# Solicitar al usuario que ingrese la fecha actual
fecha_actual_str = input("Ingrese la fecha actual (formato: dd/mm/yyyy): ")
fecha_actual = datetime.strptime(fecha_actual_str, "%d/%m/%Y")

# Calcular la fecha del Día de Muertos (2 de noviembre)
fecha_dia_de_muertos = datetime(fecha_actual.year, 11, 2)

# Calcular la fecha de Navidad (25 de diciembre)
fecha_navidad = datetime(fecha_actual.year, 12, 25)

# Calcular los días faltantes para el Día de Muertos y Navidad
dias_para_dia_de_muertos = dias_faltantes(fecha_actual, fecha_dia_de_muertos)
dias_para_navidad = dias_faltantes(fecha_actual, fecha_navidad)

# Imprimir los resultados
print("Días faltantes para el Día de Muertos:", dias_para_dia_de_muertos)
print("Días faltantes para Navidad:", dias_para_navidad)
