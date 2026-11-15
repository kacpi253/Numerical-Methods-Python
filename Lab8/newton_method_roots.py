"""
Task: newton_method_roots.py
Description: Implements Newton's method (Newton-Raphson) for finding roots using analytic derivatives.
"""

def p(x):  return x**3 - 2*x - 5
def dp(x): return 3*x**2 - 2

def q(x):  return (x - 1)**2
def dq(x): return 2*(x - 1)

def newton_analityczny(f, df, x0, tol=1e-12, max_iters=30):
    xk = x0
    for i in range(1, max_iters + 1):
        if abs(f(xk)) < tol:
            return xk, i - 1, True
            
        pochodna = df(xk)
        if pochodna == 0:
            return xk, i, False # Dzielenie przez zero
            
        xk = xk - f(xk) / pochodna
        
    return xk, max_iters, abs(f(xk)) < tol

def newton_numeryczny(f, x0, h, tol=1e-12, max_iters=30):
    xk = x0
    for i in range(1, max_iters + 1):
        if abs(f(xk)) < tol:
            return xk, i - 1, True
            
        # Wzór centralny
        pochodna = (f(xk + h) - f(xk - h)) / (2 * h)
        if pochodna == 0:
            return xk, i, False # Dzielenie przez zero
            
        xk = xk - f(xk) / pochodna
        
    return xk, max_iters, abs(f(xk)) < tol

# --- TESTY ---
print("--- Funkcja p(x) ---")
print("Analityczny:", newton_analityczny(p, dp, 2.0))
print("Num h=1e-8: ", newton_numeryczny(p, 2.0, 1e-8))
print("Num h=1e-16:", newton_numeryczny(p, 2.0, 1e-16))

print("\n--- Funkcja q(x) ---")
print("Analityczny:", newton_analityczny(q, dq, 2.0))
print("Num h=1e-8: ", newton_numeryczny(q, 2.0, 1e-8))
print("Num h=1e-16:", newton_numeryczny(q, 2.0, 1e-16))