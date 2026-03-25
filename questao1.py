import cmath

def bhaskara_comum(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' deve ser diferente de zero.")

    delta = b**2 - 4*a*c
    sqrt_delta = cmath.sqrt(delta)

    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)
    return x1, x2


def bhaskara_estavel(a, b, c):
    """
    Fórmula numericamente mais estável:
    q = -0.5 * (b + sinal(b)*sqrt(delta))
    x1 = q/a
    x2 = c/q
    """
    if a == 0:
        raise ValueError("O coeficiente 'a' deve ser diferente de zero.")

    delta = b**2 - 4*a*c
    sqrt_delta = cmath.sqrt(delta)

    if b.real >= 0:
        q = -0.5 * (b + sqrt_delta)
    else:
        q = -0.5 * (b - sqrt_delta)

    x1 = q / a
    x2 = c / q
    return x1, x2


# Testes simples
print("=== Testes simples ===")
print("x² - 5x + 6 = 0")
print("Raízes:", bhaskara_comum(1, -5, 6))   # 2 e 3

print("\nx² + 2x + 5 = 0")
print("Raízes:", bhaskara_comum(1, 2, 5))    # complexas

# Caso pedido na prova
a = 1e-8
b = -0.8
c = 1e-8

print("\n=== Equação da prova ===")
print("1e-8*x² - 0.8*x + 1e-8 = 0")

x1_comum, x2_comum = bhaskara_comum(a, b, c)
print("\nUsando fórmula comum:")
print("x1 =", x1_comum)
print("x2 =", x2_comum)

x1_est, x2_est = bhaskara_estavel(a, b, c)
print("\nUsando fórmula estável:")
print("x1 =", x1_est)
print("x2 =", x2_est)