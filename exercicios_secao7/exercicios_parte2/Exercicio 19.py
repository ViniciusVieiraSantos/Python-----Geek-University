"""
19) Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo
as seguintes informações sobre alunos de uma disciplina, sendo todas as informações do
tipo inteiro:
    . Primeira coluna: número de matrícula (use um inteiro)
    . Segunda coluna: média das provas
    . Terceira coluna: média dos trabalhos
    . Quarta coluna: nota final
(a) Leia as três primeiras informações de cada aluno.
(b) Calcule a nota final como sendo a soma da média das provas e da média
dos trabalhos.
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que
só existe uma maior nota).
(d) Imprima a média aritmética das notas finais.
"""
from random import uniform


def ler_informacoes_alunos(alunos):
    print()
    for i in range(len(alunos)):
        print(f'Aluno {alunos[i][0]}: Média das provas = {alunos[i][1]}  , Média dos trabalhos = {alunos[i][2]} ')
    print()


def notas_alunos(matricula):
    aluno = [matricula+100, round(uniform(5, 10), 1), round(uniform(5, 10), 1)]
    return aluno


def nota_final(alunos):
    nf = []
    for i in range(len(alunos)):     # somar a nota do trabalho com a prova para cada aluno e armazenar no vetor nf
        nf.append(round(alunos[i][1]+alunos[i][2], 1))

    print(f'Vetor nota final: {nf}')

    matricula_maior_nota = alunos[nf.index(max(nf))][0]
    media_notas = sum(nf) / len(nf)
    return f'Matrícula do aluno que obteve a maior nota final : {matricula_maior_nota}' \
           f'\nMédia aritmética das notas finais : {media_notas}'


matriz_alunos = [notas_alunos(i) for i in range(5)]
ler_informacoes_alunos(matriz_alunos)
print(nota_final(matriz_alunos))
