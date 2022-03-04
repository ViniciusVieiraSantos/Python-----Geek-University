"""
38) Faça uma função não-recursiva que receba um número inteiro
positivo n e retorne o fatorial exponencial desse número. Um
fatorial exponencial é um inteiro positivo n elevado à potência
de n - 1, que por sua vez é elevado à potência de n - 2 e assim
em diante. Ou seja:
n ** (n-1) ** (n-2) ...
"""


def fatorial_exponencial(numero):
    expoente = numero - 1
    for i in range(2, numero):
        expoente *= numero - i
    numero = numero ** expoente
    return numero


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Fatorial exponencial: {fatorial_exponencial(x)}')

