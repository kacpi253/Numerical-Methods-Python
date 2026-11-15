"""
Task: newton_interpolation_test.py
Description: Tests Newton interpolation using generated coefficients and evaluates the polynomial.
"""

def wyznacz_wspolczynniki_newtona(x_nodes, y_nodes):
   # Wyznacza współczynniki wielomianu interpolacyjnego Newtona 
   # metodą ilorazów różnicowych.
    
    n = len(y_nodes)
    # Kopiujemy wartości y, aby na nich przeprowadzać operacje (będą to nasze b_i)
    b = y_nodes.copy() 
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            b[i] = (b[i] - b[i - 1]) / (x_nodes[i] - x_nodes[i - j])
    return b

def horner_newton(x, b, x_nodes):
   
   # Oblicza wartość wielomianu w postaci Newtona uogólnionym schematem Hornera.
    n = len(b) - 1
    wynik = b[n]
    for i in range(n - 1, -1, -1):
        wynik = wynik * (x - x_nodes[i]) + b[i]
    return wynik

# Dane z zadania
x_wezly = [-1, 0, 2, 3]
y_wezly = [4, 1, 3, 25]

# 1) Wyznaczenie współczynników
b_wspolczynniki = wyznacz_wspolczynniki_newtona(x_wezly, y_wezly)

# 3) Wypisanie wektora współczynników
print("Wektor współczynników Newtona [b_0, b_1, b_2, b_3]:")
# Formatujemy do 4 miejsc po przecinku dla czytelności
print([round(coef, 4) for coef in b_wspolczynniki])
print("-" * 50)

# 2) Obliczanie wartości dla x = 1 oraz x = 4
punkty_badane = [1, 4]
print(f"{'x':>4} | {'Wartość wielomianu W(x)':>25}")
print("-" * 50)
for x in punkty_badane:
    wartosc = horner_newton(x, b_wspolczynniki, x_wezly)
    print(f"{x:>4} | {wartosc:>25.4f}")
