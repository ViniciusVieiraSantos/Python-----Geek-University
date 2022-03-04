"""
11) Faça um programa no qual o usuário informa o nome do arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo.
"""

x = str(input("Digite o nome do arquivo texto para ser lido: "))  # Digite 'palavras' ,para ler o arquivo existente
x += '.txt'

try:
    y = str(input('\nDigite uma palavara para procurar no arquivo: '))
    with open(x, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read().lower()
        print(texto.count(y))

except FileNotFoundError:
    print(f'Arquivo "{x}" não encontrado ')
