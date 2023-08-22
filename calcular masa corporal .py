# El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice
# de masa corporal:
# El índice de masa corporal es el cociente entre el peso del individuo en kilos y el cuadrado
# de su estatura en metros.
# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y
# le entregue su condición de riesgo.

edad =

int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso (en Kg): "))
estatura = float(input("Ingrese su estatura (en metros): "))
IMC = peso / (estatura ** 2)

print("\nEste programa calcula el IMC de una persona")
print("Para ello:\n")
print("Edad:", edad)
print("Altura:", estatura)
print("Peso:", peso)
print(" ")
print("IMC:", IMC)

if IMC < 16:
    print("Estado: Delgadez severa")
elif IMC <= 16.99:
    print("Estado: Delgadez Moderada")
elif IMC <= 18.49:
    print("Estado: Delgadez Aceptable")
elif IMC <= 24.99:
    print("Estado: Peso Normal")
elif IMC <= 29.99:
    print("Estado: Sobrepeso")
elif IMC <= 34.99:
    print("Estado: Obesidad TIPO I")
elif IMC <= 39.9:
    print("Estado: Obesidad TIPO II")
elif IMC <= 49.9:
    print("Estado: Obesidad TIPO III (obesidad morbida)")
else:
    print("Estado: Obesidad TIPO IV o Extrema")
