"""
Task: orthogonal_polynomials_moments.py
Description: Calculates moments and performs operations with orthogonal polynomials.
"""

import numpy as np

def get_moments(a, b, max_deg):
    return [(b**(k+1) - a**(k+1))/(k+1) for k in range(max_deg + 1)]

def dot(p, q, m):
    return sum(p[i]*q[j]*m[i+j] for i in range(len(p)) for j in range(len(q)))

def solve(a, b):
    m = get_moments(a, b, 15)
    P = [[0], [1.0]] 
    for k in range(1, 6):
        P_prev, P_prev2 = P[-1], P[-2]
        xP_prev = [0] + P_prev
        
        beta = -dot(xP_prev, P_prev, m) / dot(P_prev, P_prev, m)
        gamma = 0 if k == 1 else -dot(P_prev, P_prev, m) / dot(P_prev2, P_prev2, m)
        
        pk = [0] * (k + 1)
        for i, c in enumerate(xP_prev): pk[i] += c
        for i, c in enumerate(P_prev): pk[i] += beta * c
        for i, c in enumerate(P_prev2): pk[i] += gamma * c
        P.append(pk)
        
    P = P[1:] 
    print(f"\n--- Przedział [{a}, {b}] ---")
    for i, p in enumerate(P): print(f"P_{i}: {[round(c, 4) for c in p]}")
    
    max_G = max(abs(dot(P[i], P[j], m)) / np.sqrt(dot(P[i], P[i], m) * dot(P[j], P[j], m)) 
                for i in range(6) for j in range(6) if i != j)
    print(f"Max |G_ij| (i!=j): {max_G:.2e}")

solve(-1, 1)
solve(0, 1)