# Escriba un programa que reciba como entrada cuatro números, y los muestre ordenados de menor a mayor:
# Ingrese numero: 7
# Ingrese numero: 0
# Ingrese numero: 6
# Ingrese numero: 1
# 0 1 6 7
# Hay más de una manera de resolver este ejercicio

print("Este programa ordena de menor a mayor 4 números enteros, ingresados por teclado")
print("Para ello:\n")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

print("\n")

mayor = max(num1, num2, num3, num4)
menor = min(num1, num2, num3, num4)

if num1 != mayor and num1 != menor:
    medio1 = num1
elif num2 != mayor and num2 != menor:
    medio1 = num2
elif num3 != mayor and num3 != menor:
    medio1 = num3
else:
    medio1 = num4

if num1 != mayor and num1 != menor and num1 != medio1:
    medio2 = num1
elif num2 != mayor and num2 != menor and num2 != medio1:
    medio2 = num2
elif num3 != mayor and num3 != menor and num3 != medio1:
    medio2 = num3
else:
    medio2 = num4

print(menor, medio1, medio2, mayor)
