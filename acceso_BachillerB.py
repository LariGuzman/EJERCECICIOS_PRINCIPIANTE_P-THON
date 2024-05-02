def acceso_grado_superior (tiene_bachiller, ha_superado_prueba_acceso):
    if tiene_bachiller:
        return True
    elif ha_superado_prueba_acceso:
        return True
    else: 
        return False
tiene_bachiller = input ("¿Cuenta con grado de bachiller? (responda 'si' o 'no'):")
if tiene_bachiller.lower() == 'si':
    tiene_bachiller = True
else:
    tiene_bachiller = False
ha_superado_prueba_acceso = input ("¿Ha superado la prueba de acceso? (responda 'si' o 'no'):")
if ha_superado_prueba_acceso.lower() == 'si':
    ha_superado_prueba_acceso = True
else:
    ha_superado_prueba_acceso = False

puede_acceder = acceso_grado_superior (tiene_bachiller, ha_superado_prueba_acceso)

if puede_acceder:
    print("Puede acceder a cursar un ciclo formativo de grado superior.")
else:
    print("No puede acceder a cursar un ciclo formativo de grado superior.")
