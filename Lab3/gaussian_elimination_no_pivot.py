"""
Task: gaussian_elimination_no_pivot.py
Description: Implements classical Gaussian elimination method without partial pivoting.
"""

import numpy as np

def gauss_elimination_no_pivot(A, b):
    """Klasyczna eliminacja Gaussa bez wyboru elementu głównego."""
    n = len(b)
    # Tworzymy kopie robocze jako liczby zmiennoprzecinkowe (float64)
    M = A.astype(np.float64)
    v = b.astype(np.float64)

    # 1. Postępowanie proste (eliminacja)
    for k in range(n - 1):
        if M[k, k] == 0:
            raise ValueError("Zero na przekątnej - algorytm przerywa działanie.")
        
        for i in range(k + 1, n):
            m = M[i, k] / M[k, k]
            M[i, k:] = M[i, k:] - m * M[k, k:]
            v[i] = v[i] - m * v[k]

    # 2. Postępowanie odwrotne (podstawianie)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - np.dot(M[i, i+1:], x[i+1:])) / M[i, i]

    return x

# --- Testowanie dla podanych wartości epsilon ---
epsilons = [1e-2, 1e-8, 1e-12]
x_star = np.array([1.0, 1.0, 1.0])

print(f"{'Epsilon':<10} | {'Błąd względny':<20} | {'Norma residuum':<20} | {'Komentarz'}")
print("-" * 85)

for eps in epsilons:
    # Definicja macierzy i wektora b_eps
    A = np.array([
        [eps, 1.0, 1.0],
        [1.0, 1.0, 2.0],
        [1.0, 2.0, 3.0]
    ])
    b = A @ x_star
    
    # Rozwiązanie
    x_hat = gauss_elimination_no_pivot(A.copy(), b.copy())
    
    # Obliczenia błędów i residuum (norma nieskończoność)
    rel_error = np.linalg.norm(x_hat - x_star, np.inf) / np.linalg.norm(x_star, np.inf)
    residual_norm = np.linalg.norm(A @ x_hat - b, np.inf)
    

    status = "Działa poprawnie" if rel_error < 1e-5 else "Złe wyniki (niestabilność)"
    

    print(f"Eps = {eps:<10.0e} | x_hat = [{x_hat[0]:.2f}, {x_hat[1]:.2f}, {x_hat[2]:.2f}]")
    print(f"Błąd wzgl: {rel_error:.4e} | Res: {residual_norm:.4e} | {status}\n")