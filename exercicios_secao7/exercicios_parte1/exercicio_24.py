"""
24) Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura
em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do
aluno mais baixo e do mais alto, juntamente com suas alturas.
"""

alunos = {f'Aluno {i}': float(input(f'Digite a altura do aluno {i} : ')) for i in range(1, 11)}
print(f'\nAlunos : {alunos}')
print(f'Aluno mais alto  : {max(alunos, key=alunos.get)} com {alunos[max(alunos, key=alunos.get)]}m de altura')
print(f'Aluno mais baixo : {min(alunos, key=alunos.get)} com {alunos[min(alunos, key=alunos.get)]}m de altura')
