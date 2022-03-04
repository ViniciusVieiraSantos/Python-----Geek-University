"""
12) Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas
e o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais
caracteres espaços, tabulação ou nova linha.
"""
from exercicios_secao13.exercicio6 import conta_letras

try:

    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        txt = arquivo.read()
        linhas = txt.count('\n')
        print(f'\nO texto possui {len(txt) - linhas} caracteres.')
        print(f'O texto possui {linhas} linhas.')
        palavras = txt.split()
        print(f'O texto possui {len(palavras)} palavras.')
        print(f'Ocorrencia no texto de cada letra do alfabeto:\n{conta_letras(txt)}')

except FileNotFoundError:
    print(f'Arquivo "{arquivo}" não encontrado ')