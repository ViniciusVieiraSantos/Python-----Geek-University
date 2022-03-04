"""
42) Faça uma função que receba um vetor de reais e retorne a média
dele.
"""


from random import random


def calc_media(vetor):
    soma = 0
    for i in range(5):
        soma += vetor[i]
    return round(soma / len(vetor), 2)


x = [round(random() * 10, 2) for i in range(5)]
print(f'Vetor gerado: {x}')
print(f'Média : {calc_media (x)}')
