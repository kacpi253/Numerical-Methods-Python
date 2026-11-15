"""
Task: bisection_method.py
Description: Implements the bisection method to find the roots of a non-linear equation.
"""

import math

# Funkcja, której miejsca zerowego szukamy: f(x) = cos(x) - x
def f(x):
    return math.cos(x) - x

def bisekcja(a, b, tol=1e-10, max_iters=50):
    x_prev = a
    for i in range(1, max_iters + 1):
        x_k = (a + b) / 2.0
        
        # Warunek stopu: wartość funkcji bliska zeru lub znikoma zmiana x
        if abs(f(x_k)) < tol or abs(x_k - x_prev) < tol:
            return x_k, i
            
        # Zawężanie przedziału - szukamy zmiany znaku
        if f(a) * f(x_k) < 0:
            b = x_k
        else:
            a = x_k
        x_prev = x_k
        
    return x_k, max_iters

def sieczne(x0, x1, tol=1e-10, max_iters=50):
    for i in range(1, max_iters + 1):
        f0, f1 = f(x0), f(x1)
        
        # Zabezpieczenie przed dzieleniem przez zero (gdy f1 == f0)
        if f1 - f0 == 0: 
            return None, i
            
        # Główny wzór iteracyjny metody siecznych
        x_k = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        # Warunek stopu
        if abs(f(x_k)) < tol or abs(x_k - x1) < tol:
            return x_k, i
            
        # Aktualizacja punktów startowych na poczet kolejnej iteracji
        x0, x1 = x1, x_k
        
    return x_k, max_iters

# --- WYNIKI DLA ZADANIA ---
print("Zadanie 4 - Porównanie metod:")
x_bis, it_bis = bisekcja(0, 1)
print(f"Bisekcja: x = {x_bis:.10f} (zajęło {it_bis} iteracji)")

x_sie, it_sie = sieczne(0, 1)
print(f"Sieczne [0, 1]: x = {x_sie:.10f} (zajęło {it_sie} iteracji)")

print("\nZadanie 5 - Nieoptymalne dane:")
x_zle, it_zle = sieczne(5, 6)
print(f"Sieczne [5, 6]: x = {x_zle:.10f} (zajęło {it_zle} iteracji)")