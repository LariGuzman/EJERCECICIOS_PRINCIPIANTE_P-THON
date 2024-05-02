print("Ingresa año actual (formato aaaa)")
year = int(input())
print("Ingresa mes actual (formato mm)")
month = int(input())
print("Ingresa día actual (formato dd)")
day = int(input())

enero = 31
febrero = 28
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

if year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)):
    febrero = 29
    Muertos_endias = 307
    Navidad_endias = 360
    year_actual_endias = 366
else:
    febrero = 28
    Muertos_endias = 306
    Navidad_endias = 359
    year_actual_endias = 365

if (year + 1) % 4 == 0 and ((year + 1) % 100 != 0 or (year + 1) % 400 == 0):
    Muertos_siguiente_endias = 307
    Navidad_siguiente_endias = 360
    year_siguiente_endias = 366
else:
    Muertos_siguiente_endias = 306
    Navidad_siguiente_endias = 359
    year_siguiente_endias = 365

Dias_Month = 0

if month == 1:
    Dias_Month = 0
elif month == 2:
    Dias_Month = enero
elif month == 3:
    Dias_Month = enero + febrero
elif month == 4:
    Dias_Month = enero + febrero + marzo
elif month == 5:
    Dias_Month = enero + febrero + marzo + abril
elif month == 6:
    Dias_Month = enero + febrero + marzo + abril + mayo
elif month == 7:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio
elif month == 8:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio + julio
elif month == 9:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio + julio + agosto
elif month == 10:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre
elif month == 11:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre
elif month == 12:
    Dias_Month = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre
else:
    print("Elije un valor del 01 al 12 según el mes de la fecha ingresada")

fecha_endias = Dias_Month + day

# supuesto A
if fecha_endias <= Muertos_endias:
    dias_para_muertos = Muertos_endias - fecha_endias
    dias_para_navidad = Navidad_endias - fecha_endias

# supuesto B
elif fecha_endias > Muertos_endias and fecha_endias <= Navidad_endias:
    dias_para_muertos = (year_actual_endias - fecha_endias + Muertos_siguiente_endias)
    dias_para_navidad = Navidad_endias - fecha_endias

# supuesto C
elif fecha_endias > Muertos_endias and fecha_endias > Navidad_endias:
    dias_para_muertos = (year_actual_endias - fecha_endias + Muertos_siguiente_endias)
    dias_para_navidad = (year_actual_endias - fecha_endias + Navidad_siguiente_endias)

print("Faltan", dias_para_muertos, "para Día de Muertos y", dias_para_navidad, "para Navidad")
