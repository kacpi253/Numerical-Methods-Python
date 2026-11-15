# Numerical Methods - Computational Algorithms in Python 🧮

A comprehensive collection of fundamental **Numerical Methods and Computational Mathematics** algorithms implemented in pure Python. This repository demonstrates how mathematical concepts (interpolation, systems of linear equations, numerical integration, differential equations, nonlinear solvers, and approximation theory) are transformed into robust, performant software.

## 🛠️ Technology Stack & Dependencies

* **Language:** Python 3.10+
* **Dependencies:**
  * `numpy` - Matrix operations, vector arithmetic, and linear system representations.
  * `scipy` - Reference implementations (`scipy.integrate.quad`) used for error bounds and convergence verification.
  * `math` - Built-in floating-point mathematical routines.

## 📂 Implemented Algorithms & Directory Structure

The repository is organized into distinct mathematical topics:

### 1. `01_Newton_Interpolation`
* **`newton_divided_differences.py`** - Calculates the coefficients of the Newton interpolating polynomial via the divided differences tableau and evaluates the polynomial using a generalized Horner scheme.
* **`newton_interpolation_test.py`** - Test suite validating interpolation accuracy against known mathematical functions across multiple node configurations.

### 2. `02_Lagrange_Interpolation`
* **`lagrange_interpolation.py`** - Direct calculation of the Lagrange interpolating polynomial for arbitrary nodal distributions.
* **`runge_phenomenon_lagrange.py`** - Empirical simulation and analysis of Runge's phenomenon (edge oscillations occurring when high-degree polynomials use equidistant nodes).

### 3. `03_Linear_Systems_Gauss`
* **`gaussian_elimination_no_pivot.py`** - Direct Gaussian elimination algorithm with back-substitution without pivoting.
* **`gaussian_elimination_comparison.py`** - Advanced Gaussian elimination with **Partial Pivoting** (row exchange), analyzing numerical stability and mitigation of floating-point rounding errors.

### 4. `04_Numerical_Integration_Trapezoidal`
* **`trapezoidal_rule.py`** - Newton-Cotes single-interval trapezoidal quadrature formula.
* **`composite_trapezoidal_rule.py`** - Composite trapezoidal rule over $n$ subintervals with automatic convergence check against `scipy.integrate.quad`.

### 5. `05_Gauss_Legendre_Quadrature`
* **`gauss_legendre_quadrature.py`** - High-order Gauss-Legendre quadrature (2-, 3-, and 4-point weights and roots transformed from $[-1, 1]$ to arbitrary intervals).
* **`gauss_legendre_comparison.py`** - Quantitative benchmarking comparing Newton-Cotes composite methods against Gauss-Legendre quadrature.

### 6. `06_Differential_Equations_ODEs`
* **`ode_solver_euler.py`** - Initial value problem solvers: Explicit Euler method and Heun's predictor-corrector method modeling nonlinear radiation cooling.
* **`ode_solver_methods_comparison.py`** - Comparative cost-accuracy benchmark evaluating Explicit Euler, Heun, Modified Euler, and 4th-Order Runge-Kutta (**RK4**).

### 7. `07_Nonlinear_Equations_Root_Finding`
* **`bisection_method.py`** - Guaranteed-convergence bisection bracket solver for arbitrary continuous nonlinear equations.
* **`newton_method_roots.py`** - Newton-Raphson tangent method utilizing analytical derivatives for quadratic local convergence.

### 8. `08_Approximation_and_Least_Squares`
* **`least_squares_approximation.py`** - Continuous polynomial approximation via the method of least squares and Gram system construction.
* **`orthogonal_polynomials_moments.py`** - Discrete least squares approximation using orthogonal polynomials derived from moment equations.

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kacpi253/Numerical-Methods-Python.git
   cd Numerical-Methods-Python
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install numpy scipy
   ```

4. **Execute any algorithm script:**
   ```bash
   python 01_Newton_Interpolation/newton_divided_differences.py
   python 03_Linear_Systems_Gauss/gaussian_elimination_comparison.py
   python 06_Differential_Equations_ODEs/ode_solver_methods_comparison.py
   ```
