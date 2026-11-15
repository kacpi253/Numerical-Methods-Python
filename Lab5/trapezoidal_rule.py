"""
Task: trapezoidal_rule.py
Description: Implements the composite trapezoidal rule for numerical integration.
"""

import numpy as np
from scipy.integrate import quad

# Definicja funkcji
def f(x):
    return x**2 * np.sin(x)**3

# Złożony wzór trapezów
def trapezoidal(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

# Złożony wzór Simpsona
def simpson(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# Parametry
a, b = 0.5, 4.0
n_values = [4, 8, 16, 32, 64]

# b) Wartość referencyjna (z biblioteki scipy)
ref_val, _ = quad(f, a, b)

print(f"Wartość referencyjna (scipy.integrate.quad): {ref_val:.8f}\n")
print(f"{'n':<4} | {'Trapezy':<12} | {'Błąd T':<12} | {'Simpson':<12} | {'Błąd S':<12}")
print("-" * 65)

# a, c) Obliczenia i tabela błędów
for n in n_values:
    T = trapezoidal(a, b, n)
    S = simpson(a, b, n)
    err_T = abs(ref_val - T)
    err_S = abs(ref_val - S)
    print(f"{n:<4} | {T:<12.8f} | {err_T:<12.8e} | {S:<12.8f} | {err_S:<12.8e}")