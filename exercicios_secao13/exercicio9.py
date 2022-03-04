"""
9) Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo
com o conteúdo dos dois primeiros (o conteúdo do primeiro seguido do conteúdo do
segundo).
"""

x = str(input("digite o nome do arquivo texto para ser lido: "))  # Digite 'arq' ,para ler o arquivo existente
x += '.txt'

y = str(input("digite o nome do arquivo texto para ser lido: "))  # Digite 'arq2' ,para ler o arquivo existente
y += '.txt'
try:
    with open(x, 'r', encoding='utf-8') as arquivo_1:
        txt_1 = arquivo_1.read()
        with open(y, 'r', encoding='utf-8') as arquivo_2:
            txt_2 = arquivo_2.read()
            with open('arquivo3.txt', 'w', encoding='utf-8') as arquivo_3:
                arquivo_3.write(txt_1 + txt_2)


except FileNotFoundError:
    print(f'Arquivo "{x}" não encontrado ')