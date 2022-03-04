"""
17) Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em
seguida, escreva o número de alunos cuja pior nota foi na prova 1, o número
de alunos. cuja pior nota foi na prova 2, e o número de alunos cuja pior
nota foi na prova 3. Em caso de empate das piores notas de um aluno,
o critério de desempate é arbitrário, mas o aluno
deve ser contabilizado apenas uma vez.
"""
from random import randint


def imprimir_notas(notas):

    for c in range(10):
        print(f'Aluno {c + 1}:', end=' ')
        print(str(notas[c]).replace('[', '').replace(']', '').replace("'", ''))


def pior_prova(notas):
    prova = [0, 0, 0]
    for i in range(len(notas)):
        p = notas[i].index(min(notas[i]))
        prova[p] += 1
    return prova


notas_alunos = [[randint(0, 10) for j in range(3)] for i in range(10)]
imprimir_notas(notas_alunos)
piores_1, piores_2, piores_3 = pior_prova(notas_alunos)
print()
print(f'Quantida de alunos que tiraram a pior nota na 1ªprova: {piores_1}')
print(f'Quantida de alunos que tiraram a pior nota na 2ªprova: {piores_2}')
print(f'Quantida de alunos que tiraram a pior nota na 3ªprova: {piores_3}')
