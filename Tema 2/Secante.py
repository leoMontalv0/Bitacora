def secante(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        # Calcular el valor de la función en los puntos x0 y x1
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Calcular la siguiente aproximación usando la fórmula de la secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Verificar si el cambio es menor que la tolerancia
        if abs(x2 - x1) < tol:
            return x2
        
        # Actualizar los valores de x0 y x1
        x0 = x1
        x1 = x2
    
    # Si se alcanza el número máximo de iteraciones, devolver None
    print("No se encontró la raíz en el número máximo de iteraciones")
    return None

# Definir la función para la cual queremos encontrar la raíz
def funcion(x):
    return x**2 - 4

# Ejemplo de uso del método de la secante
x0 = 2.5
x1 = 3.0
raiz = secante(funcion, x0, x1)

print("La raíz encontrada es:", raiz)
