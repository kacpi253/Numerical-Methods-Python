"""
Task: ode_solver_methods_comparison.py
Description: Compares various numerical methods (Euler, Heun, Runge-Kutta) for solving ODEs based on cost and accuracy.
"""

def f(T):
    return -1e-12 * (T**4)

def exact_solution(t, T0=1200):
    return (-3 * -1e-12 * t + T0**-3)**(-1/3)

def solve_all(t_end=300, T0=1200):
    methods = {
        "Euler": {"h": 7.5, "cost": 1},
        "Heun": {"h": 15, "cost": 2},
        "Mod_Euler": {"h": 15, "cost": 2},
        "RK4": {"h": 30, "cost": 4}
    }
    
    T_exact = exact_solution(t_end)
    print(f"T_dokładne(300) = {T_exact:.4f} K\n")
    print(f"{'Metoda':<10} | {'h [s]':<5} | {'T(300) [K]':<10} | {'Błąd':<10}")
    print("-" * 45)

    for name, params in methods.items():
        h = params["h"]
        T = T0
        t = 0
        while t < t_end - 1e-9: # zabezpieczenie przed błędami zmiennoprzecinkowymi
            if name == "Euler":
                T = T + h * f(T)
            elif name == "Heun":
                k1 = f(T)
                k2 = f(T + h * k1)
                T = T + (h / 2) * (k1 + k2)
            elif name == "Mod_Euler":
                k1 = f(T)
                k2 = f(T + (h / 2) * k1)
                T = T + h * k2
            elif name == "RK4":
                k1 = f(T)
                k2 = f(T + (h / 2) * k1)
                k3 = f(T + (h / 2) * k2)
                k4 = f(T + h * k3)
                T = T + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
            t += h
            
        err = abs(T_exact - T)
        print(f"{name:<10} | {h:<5} | {T:<10.4f} | {err:<10.4f}")

solve_all()