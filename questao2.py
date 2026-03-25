import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 12*x**3 + 47*x**2 - 60*x

def df(x):
    return 4*x**3 - 36*x**2 + 94*x - 60

def newton_1d(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-14:
            raise ZeroDivisionError(f"Derivada muito próxima de zero na iteração {k}, x = {x}")

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new, k

        x = x_new

    return x, max_iter


xs = np.linspace(-1, 6, 1000)
ys = f(xs)

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, label='f(x)')
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.grid(True)
plt.legend()
plt.title("Gráfico de f(x) = x^4 - 12x^3 + 47x^2 - 60x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()


raiz, it = newton_1d(f, df, 0.5)
print("(b.1) x0 = 0.5")
print("Raiz =", raiz)
print("Iterações =", it)

raiz, it = newton_1d(f, df, 1.0)
print("\n(b.2) x0 = 1")
print("Raiz =", raiz)
print("Iterações =", it)

raiz, it = newton_1d(f, df, 2.0)
print("\n(b.3) x0 = 2")
print("Raiz =", raiz)
print("Iterações =", it)

raiz, it = newton_1d(f, df, 3.4556)
print("\n(b.4) x0 = 3.4556")
print("Raiz =", raiz)
print("Iterações =", it)

raiz, it = newton_1d(f, df, 5.5)
print("\n(b.5) x0 = 5.5")
print("Raiz =", raiz)
print("Iterações =", it)