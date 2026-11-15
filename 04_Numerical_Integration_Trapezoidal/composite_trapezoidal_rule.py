"""
Task: composite_trapezoidal_rule.py
Description: Tests the composite trapezoidal rule on specific mathematical functions to find numerical integrals.
"""

import numpy as np
from scipy.integrate import quad

def g(x):
    return np.exp(x**2) * (x - 1)

def trapezoidal(a, b, n):
    x = np.linspace(a, b, n+1)
    y = g(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def simpson(a, b, n):
    x = np.linspace(a, b, n+1)
    y = g(x)
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

a, b = -2, 2
n_values = [4, 8, 16, 32, 64]

# Wartość referencyjna
ref_val, _ = quad(g, a, b)

print(f"Wartość ref: {ref_val:.6f}\n")
print(f"{'n':<4} | {'Trapezy':<12} | {'Simpson':<12}")
print("-" * 35)

for n in n_values:
    T = trapezoidal(a, b, n)
    S = simpson(a, b, n)
    print(f"{n:<4} | {T:<12.6f} | {S:<12.6f}")