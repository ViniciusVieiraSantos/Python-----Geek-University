"""
16) Faça um programa para corrigir uma prova com 10 quetões de múltipla
escolha (a, b, c, d ou e), em uma turma com 3 alunos. Cada questão vale
1 ponto. Leia o gabarito, e para cada aluno leia sua matricula (número inteiro)
e suas respostas. Calcule e escreva: Para cada aluno, escreva sua matrícula, suas
respostas, e sua nota. O percentual de aprovação, assumindo média 7.0.
"""
from random import choice


def imprimir_aluno(matriz, matricula, nota):

    for c in range(3):
        print(f'Matricula {matricula[c]}:', end=' ')
        print(str(matriz[c]).replace('[', '').replace(']', '').replace("'", ''), end=' ')
        print(f'Nota : {nota[c]}')


def comparar_respostas(respostas):

    gabarito = ['b', 'b', 'c', 'a', 'd', 'a', 'a', 'c', 'd', 'd']
    resultado = []
    aprovados = 0
    for i in range(3):
        acerto = 0
        for j in range(10):
            x = "".join(respostas[i][j])       # converter o elemento da lista em string
            if x == gabarito[j]:
                acerto += 1
        if acerto >= 7:
            aprovados += 1
        resultado.append(acerto)
    if aprovados > 0:
        aprovados = aprovados / 3 * 100
    else:
        aprovados = 0
    return resultado, aprovados


matricula_aluno = [1102, 1103, 1104]
escolhas = ['a', 'b', 'c', 'd']
matriz_1 = [[choice(escolhas) for j in range(10)] for i in range(3)]
nota_alunos, alunos_aprovados = comparar_respostas(matriz_1)
print('\nRespostas alunos:')
imprimir_aluno(matriz_1, matricula_aluno, nota_alunos)

print(f'Percentual alunos aprovados : {alunos_aprovados} % ')
