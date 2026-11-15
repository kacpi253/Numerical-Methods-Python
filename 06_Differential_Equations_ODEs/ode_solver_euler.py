"""
Task: ode_solver_euler.py
Description: Solves ordinary differential equations (ODEs) using Euler's and Heun's methods.
"""

def f(T):
    return -1e-12 * (T**4)

def exact_solution(t, T0=1200):
    return (-3 * -1e-12 * t + T0**-3)**(-1/3)

def solve(method, h, t_end=300, T0=1200):
    T = T0
    t = 0
    steps = 0
    while t < t_end:
        if method == "Euler":
            T = T + h * f(T)
        elif method == "Heun":
            k1 = f(T)
            k2 = f(T + h * k1)
            T = T + (h / 2) * (k1 + k2)
        t += h
        steps += 1
    return T, steps

T_exact = exact_solution(300)
print(f"T_dokładne(300) = {T_exact:.2f} K\n")
print(f"{'Metoda':<8} | {'h [s]':<5} | {'T(300) [K]':<10} | {'Błąd':<10} | {'Kroki'}")
print("-" * 55)

for h in [50, 25, 10]:
    for method in ["Euler", "Heun"]:
        T_res, steps = solve(method, h)
        err = abs(T_exact - T_res)
        print(f"{method:<8} | {h:<5} | {T_res:<10.2f} | {err:<10.2f} | {steps}")
    print("-" * 55)