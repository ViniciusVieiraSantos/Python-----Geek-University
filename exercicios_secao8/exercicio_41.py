"""
41) Faça uma função que receba um vetor de inteiro e retorne o maior valor
"""


from random import randint


def maior_valor(vetor):
    return max(vetor)


x = [randint(0, 10) for i in range(5)]
print(f'Vetor gerado: {x}')
print(f'Maior valor : {maior_valor(x)}')
