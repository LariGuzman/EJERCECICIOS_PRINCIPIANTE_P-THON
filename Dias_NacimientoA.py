year_nacimiento= int(input("Ingresa año de nacimiento (formato aaaa)"))
month_nacimiento= int(input("Ingresa mes de nacimiento (formato mm)"))
day_nacimiento= int(input("Ingresa día de nacimiento (formato dd)"))
year_actual= int(input("Ingresa año actual (formato aaaa)"))
month_actual= int(input("Ingresa mes actual (formato mm)"))
day_actual= int(input("Ingresa día actual (formato dd)"))
enero=31
febrero=28
marzo=31
abril=30
mayo=31
junio=30
julio= 31
agosto=31
septiembre=30
octubre =31
noviembre=30
diciembre=31
if year_nacimiento %4==0 and ((year_nacimiento %100 !=0) or (year_nacimiento %400==0) ):
    febrero=29
Dias_Month_nacimiento = 0

if month_nacimiento == 1:
    Dias_Month_nacimiento = 0
elif month_nacimiento == 2:
    Dias_Month_nacimiento = enero
elif month_nacimiento == 3:
    Dias_Month_nacimiento = enero + febrero
elif month_nacimiento == 4:
    Dias_Month_nacimiento = enero + febrero + marzo
elif month_nacimiento == 5:
    Dias_Month_nacimiento = enero + febrero + marzo + abril
elif month_nacimiento == 6:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo
elif month_nacimiento == 7:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio
elif month_nacimiento == 8:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio + julio
elif month_nacimiento == 9:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio + julio + agosto
elif month_nacimiento == 10:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre
elif month_nacimiento == 11:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre
elif month_nacimiento == 12:
    Dias_Month_nacimiento = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre
else:
    print("Elije un valor del 01 al 12 según el mes de la fecha ingresada")
Fecha_nacimiento_endias = Dias_Month_nacimiento + day_nacimiento
if year_actual % 4 == 0 and (year_actual % 100 != 0 or year_actual % 400 == 0):
    febrero = 29
Dias_Month_actual = 0

if month_actual == 1:
    Dias_Month_actual = 0
elif month_actual == 2:
    Dias_Month_actual = enero
elif month_actual == 3:
    Dias_Month_actual = enero + febrero
elif month_actual == 4:
    Dias_Month_actual = enero + febrero + marzo
elif month_actual == 5:
    Dias_Month_actual = enero + febrero + marzo + abril
elif month_actual == 6:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo
elif month_actual == 7:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio
elif month_actual == 8:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio + julio
elif month_actual == 9:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio + julio + agosto
elif month_actual == 10:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre
elif month_actual == 11:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre
elif month_actual == 12:
    Dias_Month_actual = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre
else:
    print("Elije un valor del 01 al 12 según el mes de la fecha ingresada")

Fecha_actual_endias = Dias_Month_actual + day_actual
Dias_desde_nacimiento = 0

for i in range(year_nacimiento + 1, year_actual):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        Dias_desde_nacimiento = Dias_desde_nacimiento + 366
    else:
        Dias_desde_nacimiento = Dias_desde_nacimiento + 365
if year_nacimiento %4==0 and ((year_nacimiento %100 !=0) or (year_nacimiento %400==0) ):
    Dias_desde_nacimiento= Dias_desde_nacimiento+(366-Fecha_nacimiento_endias)+Fecha_actual_endias
else:
        Dias_desde_nacimiento= Dias_desde_nacimiento+(365-Fecha_nacimiento_endias)+Fecha_actual_endias
print ("Haz vivido ", Dias_desde_nacimiento, "días")