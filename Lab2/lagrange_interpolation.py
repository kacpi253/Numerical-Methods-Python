"""
Task: lagrange_interpolation.py
Description: Implements Lagrange interpolation for a given set of nodes.
"""

import math

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

# Dane wejściowe
x_nodes = [0.0, 0.25, 0.5, 0.75, 1.0]
y_nodes = [math.log(1 + x) for x in x_nodes] # f(x) = ln(1+x)
x_target = 0.43

# a) Obliczenie wartości interpolantu P(0.43)
p_43 = lagrange_interpolation(x_target, x_nodes, y_nodes)

# b) Wartość dokładna f(0.43) i błąd
f_43 = math.log(1 + x_target)
error_lagrange = abs(p_43 - f_43)

# c) Interpolacja liniowa (tylko na dwóch najbliższych węzłach: 0.25 i 0.5)
x_lin_nodes = [0.25, 0.5]
y_lin_nodes = [math.log(1 + x) for x in x_lin_nodes]
p_lin_43 = lagrange_interpolation(x_target, x_lin_nodes, y_lin_nodes)
error_lin = abs(p_lin_43 - f_43)

# Wypisanie wyników
print(f"a) P(0.43) = {p_43:.5f}")
print(f"b) f(0.43) = {f_43:.5f} | Błąd Lagrange'a (st. 4): {error_lagrange:.5f}")
print(f"c) P_lin(0.43) = {p_lin_43:.5f} | Błąd interpolacji liniowej: {error_lin:.5f}")