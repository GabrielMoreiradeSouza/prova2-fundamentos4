import numpy as np

def F(x):
    x1, x2 = x
    return np.array([
        x1 + x2 - 3,
        x1**2 + x2**2 - 9
    ], dtype=float)

def J(x):
    x1, x2 = x
    return np.array([
        [1, 1],
        [2*x1, 2*x2]
    ], dtype=float)

def newton_sistema(F, J, x0, tol=1e-5, max_iter=100):
    x = np.array(x0, dtype=float)

    for k in range(1, max_iter + 1):
        Fx = F(x)
        Jx = J(x)

        delta = np.linalg.solve(Jx, -Fx)
        x_new = x + delta

        erro = np.linalg.norm(delta, ord=np.inf)
        print(f"Iteração {k}: x = {x_new}, erro = {erro}")

        if erro < tol:
            return x_new, k

        x = x_new

    return x, max_iter


x0 = [1, 5]
solucao, iteracoes = newton_sistema(F, J, x0, tol=1e-5)

print("\nSolução aproximada:", solucao)
print("Número de iterações:", iteracoes)