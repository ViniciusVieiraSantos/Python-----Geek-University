"""
35) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o fatorial quádruplo desse número. O fatorial quádruplo de um número n é dado
por: (2 * n)! / n!
"""


def fatorial_quaduplo(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= (2 * i) / i
    return fatorial


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Fatorial quadruplo: {fatorial_quaduplo(x)}')
