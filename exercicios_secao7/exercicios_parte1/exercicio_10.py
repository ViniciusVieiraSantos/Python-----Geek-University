"""
10) Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
calcule e imprima a média geral.
"""

notas = [int(input(f'Nota do aluno {i} : ')) for i in range(1, 16)]

print(f'Notas : {notas}\n Media geral = {round(sum(notas)/len(notas),1)}')
