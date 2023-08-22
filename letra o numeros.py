# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos.
# En caso que sea letra, determine si es mayúscula o minúscula.
# TIP: Para cada caracter es asignado un valor entero (Correspondiente al código ASCII),
# usted puede aprovechar esto para hacer sus comparaciones de manera más sencilla.
# EJ:
# La letra 'a' corresponde al valor entero 97.

caracter = int(input("Ingrese el número del caracter a analizar (Según el número de código código ASCII): "))

if caracter >= 97 and caracter <= 122:
    print("El caracter es una letra minúscula.")
else:
    if caracter >= 65 and caracter <= 90:
        print("El caracter es una letra mayúscula.")
    else:
        if caracter >= 48 and caracter <= 57:
            print("El caracter es un número.")
        else:
            if caracter >= 128 and caracter <= 255:
                print("El caracter es un caracter ASCII extendido NO IMPRIMIBLE.")
            else:
                print("El caracter no es ni una letra ni un número.")
