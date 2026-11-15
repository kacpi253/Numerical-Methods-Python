"""
Task: gaussian_elimination_comparison.py
Description: Compares Gaussian elimination with and without partial pivoting for solving systems of linear equations.
"""

import numpy as np

# --- Metoda z Zadania 3 (bez pivota) do porównania ---
def gauss_no_pivot(A, b):
    n = len(b)
    M, v = A.astype(np.float64), b.astype(np.float64)
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = M[i, k] / M[k, k]
            M[i, k:] = M[i, k:] - m * M[k, k:]
            v[i] = v[i] - m * v[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - np.dot(M[i, i+1:], x[i+1:])) / M[i, i]
    return x

# --- Metoda z Zadania 4 (Gauss-Crout, zamiana kolumn) ---
def gauss_column_pivoting(A, b):
    n = len(b)
    M, v = A.astype(np.float64), b.astype(np.float64)
    p = np.arange(n) # Tablica śledząca permutacje (kolejność niewiadomych)
    
    for k in range(n - 1):
        # Szukamy największego elementu w aktualnym wierszu (od k do końca)
        max_col = np.argmax(np.abs(M[k, k:])) + k
        
        # Zamiana kolumn i aktualizacja permutacji
        if max_col != k:
            M[:, [k, max_col]] = M[:, [max_col, k]]
            p[k], p[max_col] = p[max_col], p[k]
            
        # Standardowa eliminacja
        for i in range(k + 1, n):
            m = M[i, k] / M[k, k]
            M[i, k:] = M[i, k:] - m * M[k, k:]
            v[i] = v[i] - m * v[k]
            
    # Postępowanie odwrotne
    y = np.zeros(n)
    for i in range(n - 1, -1, -1):
        y[i] = (v[i] - np.dot(M[i, i+1:], y[i+1:])) / M[i, i]
        
    # Odtworzenie prawidłowej kolejności niewiadomych x
    x = np.zeros(n)
    for i in range(n):
        x[p[i]] = y[i]
        
    return x

# --- Testowanie Przypadku I (Mały pivot) ---
print("--- Przypadek I: Mały pivot (B) ---")
B = np.array([[1e-8, 1.0, 1.0], [1.0, 1.0, 2.0], [1.0, 2.0, 3.0]])
x_star_1 = np.ones(3)
b_1 = B @ x_star_1

x_no_pivot_1 = gauss_no_pivot(B.copy(), b_1.copy())
x_pivot_1 = gauss_column_pivoting(B.copy(), b_1.copy())

print(f"Bez pivota -> Błąd: {np.linalg.norm(x_no_pivot_1 - x_star_1, np.inf):.2e} | Res: {np.linalg.norm(B @ x_no_pivot_1 - b_1, np.inf):.2e}")
print(f"Z pivotem  -> Błąd: {np.linalg.norm(x_pivot_1 - x_star_1, np.inf):.2e} | Res: {np.linalg.norm(B @ x_pivot_1 - b_1, np.inf):.2e}\n")


# --- Testowanie Przypadku II (Macierz Hilberta H6) ---
print("--- Przypadek II: Macierz Hilberta (H6) ---")
H6 = np.zeros((6, 6))
for i in range(1, 7):
    for j in range(1, 7):
        H6[i-1, j-1] = 1.0 / (i + j - 1)
        
x_star_2 = np.ones(6)
b_2 = H6 @ x_star_2

x_no_pivot_2 = gauss_no_pivot(H6.copy(), b_2.copy())
x_pivot_2 = gauss_column_pivoting(H6.copy(), b_2.copy())

print(f"Bez pivota -> Błąd: {np.linalg.norm(x_no_pivot_2 - x_star_2, np.inf):.2e} | Res: {np.linalg.norm(H6 @ x_no_pivot_2 - b_2, np.inf):.2e}")
print(f"Z pivotem  -> Błąd: {np.linalg.norm(x_pivot_2 - x_star_2, np.inf):.2e} | Res: {np.linalg.norm(H6 @ x_pivot_2 - b_2, np.inf):.2e}")