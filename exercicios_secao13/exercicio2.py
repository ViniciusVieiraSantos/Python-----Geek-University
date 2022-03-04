"""
2) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas linhas esse arquivo possui
"""

x = input("digite o nome do arquivo texto para ser lido: ")
x += '.txt'

try:
    with open(x, 'r') as arquivo:
        linhas = arquivo.readlines()
        print(len(linhas))

except FileNotFoundError:
    print(f'Arquivo "{x}" não encontrado ')
