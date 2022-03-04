"""
14) Dado um arquivo contendo um conjunto de nome e data nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada
pessoa do primeiro arquivo.
"""
from datetime import date


def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


try:
    with open('nomes.txt', 'r', encoding='utf-8') as arquivo_1:
        linhas = arquivo_1.readlines()

        # Cria uma lista separando as informacoes, onde o ultimo elemento da lista é a data de nascimento
        informacao = [linhas[i].strip().split() for i in range(len(linhas))]

        # Criar outra lista retirando a data do final da linha e separando dia,mes e ano
        data_nasc = [informacao[i].pop().split("/") for i in range(len(informacao))]
        data_nasc = [[int(data) for data in pessoa] for pessoa in data_nasc]

        with open('nomes_idade.txt', 'w', encoding='utf-8')as arquivo_2:
            for i in range(len(informacao)):
                arquivo_2.write(f'{" ".join(informacao[i])}  '
                                f'{str(calculateAge(date(data_nasc[i][2], data_nasc[i][1], data_nasc[i][0])))}\n')

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

