def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de bisección para encontrar la raíz de la ecuación f(x) = 0
    :param f: Función para la cual se busca la raíz
    :param a: Límite inferior del intervalo
    :param b: Límite superior del intervalo
    :param tol: Tolerancia para el error
    :param max_iter: Número máximo de iteraciones
    :return: Raíz aproximada
    """
    # Verificar si el cambio de signo es válido en el intervalo
    if f(a) * f(b) > 0:
        print("No hay un cambio de signo en el intervalo, no se puede aplicar el método de bisección.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol:  # Convergencia basada en el tamaño del intervalo
        c = (a + b) / 2  # Punto medio
        if f(c) == 0:  # Si encontramos la raíz exacta
            break
        elif f(a) * f(c) < 0:  # Si el cambio de signo es entre a y c
            b = c
        else:  # Si el cambio de signo es entre c y b
            a = c
        
        iter_count += 1
        if iter_count >= max_iter:  # Control de iteraciones
            print("Se alcanzó el número máximo de iteraciones.")
            break
    
    # Raíz aproximada
    c = (a + b) / 2
    print(f"Raíz aproximada: {c}")
    print(f"Error relativo: {abs(f(c))}")
    return c

# Ejemplo de uso: encontrar la raíz de f(x) = e^(-x) - x en el intervalo [0, 1]
import math

def f(x):
    return math.exp(-x) - x

# Llamada al método de bisección
raiz = bisection_method(f, 0, 1)


