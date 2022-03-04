"""
21) Faça um programa que receba do usuário dois vetores, A e B,
com 10 números inteiros cada. Crie um novo vetor denominado C
calculando C = A - B. Mostre na tela os dados do vetor C
"""

from random import randint

a = [randint(1, 20) for i in range(10)]
b = [randint(1, 20) for j in range(10)]
print(f'\nVetor A : {a}  Vetor B : {b}\n')

c = [a[i] - b[i] for i in range(10)]
print(f'Vetor C (A-B): {c}')
