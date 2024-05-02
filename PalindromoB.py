def es_palindromo(frase):
    # Eliminar los espacios en blanco y convertir la frase a minúsculas
    frase = ''.join(caracter for caracter in frase if caracter.isalnum()).lower()
    # Comparar la frase original con su reverso
    return frase == frase[::-1]

# Solicitar al usuario que ingrese una palabra o frase
palabra_frase = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

# Verificar si la palabra o frase es un palíndromo e imprimir el resultado
if es_palindromo(palabra_frase):
    print("La palabra o frase es un palíndromo.")
else:
    print("La palabra o frase no es un palíndromo.")
