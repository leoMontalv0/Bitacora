import math

# Definir la función f(x) y su derivada f'(x)
def f(x):
    return x**3 + 6*x - 27

def df(x):
    return 3*x**2 + 6

# Método de Newton-Raphson
def newton_raphson(x0, tol=0.001, max_iter=10):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)  # Fórmula de Newton-Raphson
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return None, max_iter  

# Parámetros iniciales
x0 = 4 # Punto de inicio
raiz, iteraciones = newton_raphson(x0)

# Mostrar resultado
if raiz:
    print(f"La raíz aproximada es: {raiz:.3f}")
    print(f"Número de iteraciones: {iteraciones}")
else:
    print("El método no funcionó")
