"""
37) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o hiperfatorial desse número. O hiperfatorial de um número n,
escrito H(n), é definido por:
H(n) = | | n / k=1  k**k = 1**1 . 2**2 . 3**3 ... (n - 1) ** n-1 . n**n
"""
def hiper_fatorial(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i ** i
    return fatorial


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Hiper fatorial: { hiper_fatorial(x)}')
