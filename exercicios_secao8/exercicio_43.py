"""
43) Faça uma função que receba um vetor de inteiros e o preencha
com números aleatórios sem repetição.
"""

from random import randint


def gera_vetor(tamanho):
    lista = []
    for i in range(0, tamanho):
        valor = randint(0, 100)
        while valor in lista:
            valor = randint(0, 100)
        lista.append(valor)
    return lista


x = int(input('Tamanho do vetor : '))
print(f'Vetor gerado : {gera_vetor (x)}')

