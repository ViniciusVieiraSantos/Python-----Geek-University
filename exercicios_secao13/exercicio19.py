"""
19) Faça um programa que receba do usuário um arquivo que contenha o nome
e a nota de diversos alunos.txt (da seguinte forma: NOME:JOÃO NOTA:8), um aluno
por linha. Mostre na tela o nome e a nota do aluno que possui a maior nota.
"""
try:
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.read().split('\n')

        # Para cada aluno ,cria uma sublista onde a ultima posicao é a nota do aluno, e as demais são o nome do aluno
        linhas = [linha.split() for linha in linhas]

        # para separar as notas ,foi utilizado 'pop()' para remover as notas de cada aluno do vetor 'linhas',em seguida
        # foi utilizado split() com o argumento ':' para separar a string do inteiro,o que gerou uma sublista
        # '['Nota','valor da nota'] e entao foi utilizado 'pop()' para pegar o valor da nota e salvar no vetor notas
        notas = [int(linhas[i].pop().split(':').pop()) for i in range(len(linhas))]

        nomes = [' '.join(linhas[i]).title() for i in range(len(linhas))]

        dict_notas = {nomes[i]: notas[i] for i in range(len(notas))}
        maior_nota = (max(dict_notas, key=lambda x: dict_notas[x]))

        print(f'\nMaior nota:\n{maior_nota} : {dict_notas[maior_nota]}')

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")