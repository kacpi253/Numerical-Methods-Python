"""
Task: gauss_legendre_quadrature.py
Description: Implements Gauss-Legendre quadrature for numerical integration mapping to [a, b].
"""

import numpy as np

def gauss_legendre(f, a, b, n):
    # Pobranie węzłów (x) i wag (w) na standardowym przedziale [-1, 1]
    x, w = np.polynomial.legendre.leggauss(n)
    
    # Przeskalowanie węzłów z [-1, 1] na docelowy przedział [a, b]
    x_mapped = 0.5 * (b - a) * x + 0.5 * (a + b)
    
    # Przeskalowanie wag i obliczenie całki
    integral = 0.5 * (b - a) * np.sum(w * f(x_mapped))
    return integral

# Zdefiniowanie funkcji podcałkowych
f1 = lambda x: np.exp(x)
f2 = lambda x: 1 / (1 + 25 * x**2)

# Dokładne wartości całek do obliczenia błędów
I1_exact = np.e - 1
I2_exact = (2 * np.arctan(5)) / 5

# Wypisywanie wyników
print("n |    I1 (e^x) |     Błąd I1 |  I2 (Runge) |     Błąd I2")
print("-" * 55)
for n in [2, 3, 4, 5]:
    I1_val = gauss_legendre(f1, 0, 1, n)
    I2_val = gauss_legendre(f2, -1, 1, n)
    
    err1 = abs(I1_val - I1_exact)
    err2 = abs(I2_val - I2_exact)
    
    print(f"{n} | {I1_val:.7f} | {err1:.3e} | {I2_val:.7f} | {err2:.3e}")