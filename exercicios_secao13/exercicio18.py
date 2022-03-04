"""
18) Faça um programa que leia um arquivo contendo o nome e o preço de diversos
produtos (separados por linha), e calcule o total da compra.
"""


try:
    with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.read().split('\n')
        linhas = [linha.split() for linha in linhas]

        precos = [int(linhas[i][-1]) for i in range(len(linhas))]
        print(f'Total da compra : {sum(precos)}')

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
