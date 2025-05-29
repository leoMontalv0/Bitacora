import numpy as np

def f(x):
    return np.exp(-x) - x

def regla_falsa(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError(f"El intervalo [{a}, {b}] no cambia de signo. f(a)={f(a)}, f(b)={f(b)}")

    for _ in range(max_iter):
        xr = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(xr)) < tol:
            return xr

        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr

    return xr

raiz = regla_falsa(f, 0, 1)

print(f"La raíz aproximada es: {raiz:.3g}")

