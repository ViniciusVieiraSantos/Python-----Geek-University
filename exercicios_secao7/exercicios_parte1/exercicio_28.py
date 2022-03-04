"""
28) Leia 10 números inteiros e armazene em um vetor v. Crie
dois novos vetores v1 e v2. Copie os valores ímpares de v para v1,
e os valores pares de v para v2. Note que cada um dos valores v1 e v2
têm no máximo 10 elementos, mas nem todos os elementos são utilizados.
No final escreva os elementos UTILIZADOS de v1 e v2.
"""
from random import randint

vetor = [randint(1, 20) for i in range(10)]
print(f'\nVetor : {vetor}')

v1 = [valor for valor in vetor if valor % 2 != 0]
v2 = [valor for valor in vetor if valor % 2 == 0]


print(f'Vetor 1 : {v1}')
print(f'Vetor 2 : {v2}')
