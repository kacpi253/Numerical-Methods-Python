"""
Task: newton_divided_differences.py
Description: Calculates coefficients of the Newton interpolation polynomial using divided differences.
"""

def wyznacz_wspolczynniki_newtona(x_nodes, y_nodes):
 
   # 1) Wyznacza współczynniki wielomianu interpolacyjnego Newtona metodą ilorazów różnicowych.
    
    n = len(y_nodes)
    b = y_nodes.copy() 
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            b[i] = (b[i] - b[i - 1]) / (x_nodes[i] - x_nodes[i - j])
    return b

def horner_newton(x, b, x_nodes):
  
   # 2) Oblicza wartość wielomianu w postaci Newtona uogólnionym schematem Hornera.
   
    n = len(b) - 1
    wynik = b[n]
    for i in range(n - 1, -1, -1):
        wynik = wynik * (x - x_nodes[i]) + b[i]
    return wynik

# Dane z zadania
x_wezly = [-1, 0, 2, 3]
y_wezly = [4, 1, 3, 25]


b_wspolczynniki = wyznacz_wspolczynniki_newtona(x_wezly, y_wezly)

print("Wektor współczynników Newtona [b_0, b_1, b_2, b_3]:")
print([round(coef, 4) for coef in b_wspolczynniki])
print("-" * 60)

# 3) Obliczanie wartości dla x = 1 oraz x = 4
punkty_badane = [1, 4]
print(f"{'x':>4} | {'Wartość wielomianu W(x)':>25}")
print("-" * 60)
for x in punkty_badane:
    wartosc = horner_newton(x, b_wspolczynniki, x_wezly)
    print(f"{x:>4} | {wartosc:>25.4f}")

# 4) Interpretacja wyników wypisywana przez program
print("-" * 60)
print("INTERPRETACJA WYNIKÓW:")
print("Dla x = 1: Otrzymano wartość ok. -2.1667. Jest to proces INTERPOLACJI,")
print("ponieważ punkt znajduje się wewnątrz przedziału węzłów [-1, 3].")
print("Wynik ten jest wysoce wiarygodny.")
print()
print("Dla x = 4: Otrzymano wartość ok. 72.3333. Jest to proces EKSTRAPOLACJI,")
print("ponieważ punkt leży poza przedziałem węzłów. Widać tu typowy dla")
print("wielomianów gwałtowny wzrost wartości na zewnątrz przedziału,")
print("przez co wynik ten charakteryzuje się bardzo niskim zaufaniem.")
