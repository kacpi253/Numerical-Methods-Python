"""
Task: runge_phenomenon_lagrange.py
Description: Demonstrates the Runge's phenomenon using Lagrange interpolation on equidistant nodes.
"""

import math

# Badana funkcja (funkcja Rungego )
def f(x):
    return 1.0 / (1.0 + 25.0 * x**2)

# Funkcja realizująca interpolację Lagrange'a
def lagrange_interpolation(x_target, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term = term * (x_target - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Ustawienia początkowe
n_nodes = 11  # 11 węzłów = wielomian 10. stopnia

# 1. Węzły równoodległe
x_eq = [-1.0 + 2.0 * i / (n_nodes - 1) for i in range(n_nodes)]
y_eq = [f(x) for x in x_eq]

# 2. Węzły Czebyszewa
x_cheb = [math.cos(k * math.pi / 10.0) for k in range(n_nodes)]
y_cheb = [f(x) for x in x_cheb]

# Gęsta siatka 1001 punktów w przedziale [-1, 1]
n_grid = 1001
x_grid = [-1.0 + 2.0 * i / (n_grid - 1) for i in range(n_grid)]

max_err_eq = 0.0
max_err_eq_x = 0.0
max_err_cheb = 0.0
max_err_cheb_x = 0.0

# Poszukiwanie maksymalnego błędu
for x in x_grid:
    exact = f(x)
    
    # Błąd dla węzłów równoodległych
    err_eq = abs(lagrange_interpolation(x, x_eq, y_eq) - exact)
    if err_eq > max_err_eq:
        max_err_eq = err_eq
        max_err_eq_x = x
        
    # Błąd dla węzłów Czebyszewa
    err_cheb = abs(lagrange_interpolation(x, x_cheb, y_cheb) - exact)
    if err_cheb > max_err_cheb:
        max_err_cheb = err_cheb
        max_err_cheb_x = x

# Obliczenia dla ekstrapolacji (x=1.2)
x_ext = 1.2
p_eq_ext = lagrange_interpolation(x_ext, x_eq, y_eq)
p_cheb_ext = lagrange_interpolation(x_ext, x_cheb, y_cheb)
f_ext = f(x_ext)


# Wypisanie wyników
print(f"a) Max błąd (równoodległe): {max_err_eq:.5f}")
print(f"a) Max błąd (Czebyszew):    {max_err_cheb:.5f}")
print(f"b) Najgorszy punkt (równoodległe): x = {max_err_eq_x:.3f}")
print(f"b) Najgorszy punkt (Czebyszew):    x = {max_err_cheb_x:.3f}")
print(f"c) P_równo(1.2) = {p_eq_ext:.2f} | P_Czeb(1.2) = {p_cheb_ext:.2f} | f(1.2) = {f_ext:.5f}")