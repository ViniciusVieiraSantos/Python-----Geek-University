"""
59) Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos
inteiros e que calcule e retorne, taambém por parâmetro, o vetor união
dos dois primeiros.
"""

from random import randint


def uniao_vetor(vetor_1, vetor_2):
    uniao = list(set().union(vetor_1, vetor_2))
    return uniao


vet_1 = [randint(0, 40) for i in range(10)]
vet_2 = [randint(0, 40) for j in range(10)]


print(f'Vetor 1:{vet_1}')
print(f'Vetor 2:{vet_2}')
print(f'Vetor union:{uniao_vetor(vet_1, vet_2)}')
