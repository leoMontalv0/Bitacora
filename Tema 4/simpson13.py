import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi

def simpson_13_interactivo():
    """
    Programa interactivo para calcular integrales definidas usando la regla de Simpson 1/3.
    Versión corregida para manejar funciones con numpy.
    """
    # Mostrar encabezado e instrucciones para el usuario
    print("=== Calculadora de Integrales por Regla de Simpson 1/3 ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x**2)'")
    print("4. El número de subintervalos (n) debe ser par (si ingresa impar, se ajustará)")

    # Entrada de datos
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0, preferiblemente par): "))

    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return
