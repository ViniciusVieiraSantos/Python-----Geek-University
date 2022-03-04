"""
26) Faça um algoritmo que receba um número inteiro positivo n e calcule o
somatório de 1 até n.
"""


def soma_numeros(numero):
    soma = 0
    for i in range(1, numero):
        soma += i
    return soma


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'soma dos numeros de 1 a {x} : {soma_numeros(x)}')
