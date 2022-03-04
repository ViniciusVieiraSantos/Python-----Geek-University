"""
28) Faça um programa que recebe como entrada o nome de um arquivo
de entrada e o nome de um arquivo de saída. Cada linha do arquivo
de entrada possui colunas de tamanho de 30 caracteres. No arquivo de saída
deverá ser escrito o arquivo de entrada de forma inversa. Veja um exemplo:
Arquivo de entrada:
Hoje é dia de prova de AP
A prova está muito fácil
vou tirar uma boa nota
Arquivo de saída
Aton aob amu ratir uov
Licáf otium átse avorp A
PA ed avortp ed aid é ejoH
"""


try:
    with open(f'texto_28.txt', 'r', encoding='utf-8')as arquivo:
        texto = arquivo.read()
    texto = texto[::-1]
    with open('texto_28_reverso.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
except FileNotFoundError:
    print('Arquivo não existe')