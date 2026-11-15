"""
Task: least_squares_approximation.py
Description: Applies least squares approximation techniques using orthogonal polynomials and moments.
"""

import numpy as np
from scipy.integrate import quad

def get_moments(a, b, max_deg):
    return [(b**(k+1) - a**(k+1))/(k+1) for k in range(max_deg + 1)]

def dot(p, q, m):
    return sum(p[i]*q[j]*m[i+j] for i in range(len(p)) for j in range(len(q)))

m_mom = get_moments(0, 1, 15)
P = [[0], [1.0]] 
for k in range(1, 7): # generujemy do P_6 dla m=6
    P_prev, P_prev2 = P[-1], P[-2]
    xP_prev = [0] + P_prev
    beta = -dot(xP_prev, P_prev, m_mom) / dot(P_prev, P_prev, m_mom)
    gamma = 0 if k == 1 else -dot(P_prev, P_prev, m_mom) / dot(P_prev2, P_prev2, m_mom)
    pk = [0] * (k + 1)
    for i, c in enumerate(xP_prev): pk[i] += c
    for i, c in enumerate(P_prev): pk[i] += beta * c
    for i, c in enumerate(P_prev2): pk[i] += gamma * c
    P.append(pk)
P = P[1:]

def eval_p(p, x): return sum(c * x**i for i, c in enumerate(p))

C = []
for k in range(7):
    num, _ = quad(lambda x: np.exp(x) * eval_p(P[k], x), 0, 1) # całka numeryczna
    den = dot(P[k], P[k], m_mom)
    C.append(num / den)

print("a) Współczynniki c_k:")
for k, c in enumerate(C): print(f"c_{k} = {c}")

print("\nb) Błędy:")
x_grid = np.linspace(0, 1, 1005)
for m in [2, 4, 6]:
    f_m = lambda x: sum(C[k] * eval_p(P[k], x) for k in range(m + 1))
    max_err = max(abs(np.exp(x) - f_m(x)) for x in x_grid)
    l2_err_sq, _ = quad(lambda x: (np.exp(x) - f_m(x))**2, 0, 1)
    print(f"m={m}: błąd L2 = {np.sqrt(l2_err_sq):.2e}, błąd Max = {max_err:.2e}")