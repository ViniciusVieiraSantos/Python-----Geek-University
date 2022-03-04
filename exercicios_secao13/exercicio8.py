"""
8) Faça um programa que leia o conteúdo de um arquivo e crie um arquivo
com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função
que converte maiúscula para minúscula é o toupper(). Ela é aplicada em cada caractere da string.
"""

x = str(input("digite o nome do arquivo texto para ser lido: "))  # Digite 'arq' ,para ler o arquivo existente
x += '.txt'
try:

    with open(x, 'r', encoding='utf-8') as arquivo:
        txt = arquivo.read()
        print(f'Arquivo original :\n{txt}')

        with open('novo_arquivo.txt', 'w', encoding='utf-8') as novo_arquivo:
            novo_arquivo.write(txt.upper())

except FileNotFoundError:
    print(f'Arquivo "{x}" não encontrado ')
