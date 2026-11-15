"""
Task: gauss_legendre_comparison.py
Description: Compares Gauss-Legendre quadrature integration results with scipy's quad function.
"""

import numpy as np
from scipy.integrate import quad

f = lambda x: x**2 * np.sin(x)**3
a, b = 0, 4.5

def gauss(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * np.sum(w * f(0.5 * (b - a) * x + 0.5 * (a + b)))

def zlozona_gauss(f, a, b, m, n=2):
    xp = np.linspace(a, b, m+1)
    return sum(gauss(f, xp[i], xp[i+1], n) for i in range(m))

# Wartość referencyjna (z biblioteki scipy)
ref, _ = quad(f, a, b)

print(f"Ref: {ref:.6f}\n")
print(f"{'Metoda':<15} | {'Wynik':<9} | {'Błąd':<9} | {'Koszt'}")
print("-" * 45)

I5 = gauss(f, a, b, 5)
print(f"1-przedz (n=5)  | {I5:.6f} | {abs(I5-ref):.2e} | 5")

for m in [2, 4, 8, 16]:
    Iz = zlozona_gauss(f, a, b, m)
    print(f"Złożona (m={m:<2}) | {Iz:.6f} | {abs(Iz-ref):.2e} | {m*2}")