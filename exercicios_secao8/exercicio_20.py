"""
20) Faça um algoritmo que receba um número inteiro positivo n
e calcule o seu fatorial, n!
"""


def calcular_fatorial(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    return fatorial


x = int(input('Digite um numero para ser fatorado: '))
print(f'{x}! = {calcular_fatorial(x)}')
