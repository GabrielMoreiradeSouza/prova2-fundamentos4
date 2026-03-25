import numpy as np

def jacobi(A, b, x0, tol=1e-5, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)

    n = len(b)
    D = np.diag(A)
    R = A - np.diagflat(D)

    if np.any(D == 0):
        raise ValueError("A matriz possui zero na diagonal principal.")

    for k in range(1, max_iter + 1):
        x_new = (b - np.dot(R, x)) / D

        erro = np.linalg.norm(x_new - x, ord=np.inf)
        print(f"Iteração {k}: x = {x_new}, erro = {erro}")

        if erro < tol:
            return x_new, k

        x = x_new

    return x, max_iter


A = [
    [10, 3, -2],
    [2, 8, -1],
    [1, 1, 5]
]

b = [57, 20, -4]
x0 = [0, 0, 0]

solucao, iteracoes = jacobi(A, b, x0, tol=1e-5)

print("\nSolução aproximada:", solucao)
print("Número de iterações:", iteracoes)