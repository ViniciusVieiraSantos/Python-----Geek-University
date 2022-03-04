"""
40) Faça uma função que receba um vetor de inteiros e retorne
quantos valores pares ele possui.
"""


from random import randint


def conta_var(vetor):
    cont = 0
    for i in range(5):
        if vetor[i] % 2 == 0:
            cont += 1
    return cont


x = [randint(0, 10) for i in range(5)]
print(f'Vetor gerado: {x}')
print(f'Numeros pares no vetor : {conta_var(x)}')

