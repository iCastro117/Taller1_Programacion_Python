# Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de
# los lados no puede ser más largo que la suma de los otros dos.
# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
# ● si acaso el triángulo es inválido; y
# ● si no lo es, qué tipo de triángulo es.
# 1) Triángulo equilátero. Tres lados iguales.
# 2) Triángulo isósceles. Dos lados iguales.
# 3) Triángulo escaleno. Tres lados desiguales

a = float(input("Ingrese la medida del lado A: "))
b = float(input("Ingrese la medida del lado B: "))
c = float(input("Ingrese la medida del lado C: "))

print("\nEste programa calcula el Tipo de Triangulo, segun la medida de sus 3 lados")
print("Para ello:\n")

# Operaciones de Desigualdad de Triangulos

# Triángulo equilátero (Tres lados iguales)
if a == b == c:
    print("Es un triángulo Equilátero")
# Triángulo isósceles (Dos lados iguales)
elif a == b or b == c or a == c:
    print("Es un triángulo Isósceles")
# Triángulo escaleno (Tres lados desiguales)
elif a + b > c and b + c > a and a + c > b:
    print("Es un triángulo Escaleno")
else:
    print("No es un triángulo válido")
