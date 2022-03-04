"""
7) Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo
texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'
"""


def substitui_vogais(texto):
    """
    Recebe uma string , substitui as vogais por '*' e cria um novo arquivo
    :param texto:
    :return: None
    """
    try:
        vogais = ['a', 'e', 'i', 'o', 'u']
        texto = texto.lower()
        for vogal in vogais:
            texto = texto.replace(vogal, '*')
        with open('arq_novo', 'w+', encoding='utf-8') as arquivo_n:
            arquivo_n.write(texto)

    except AttributeError:
        return ' AttributeError, o parametro passado deve ser uma string'


if __name__ == '__main__':
    x = str(input("\nDigite o nome do arquivo texto para ser lido: "))   # Digite 'arq2' ,para ler o arquivo existente
    x += '.txt'
    try:

        with open(x, 'r', encoding='utf-8') as arquivo:
            txt = arquivo.read()
            print(f'\nArquivo originial:\n{txt}')
            substitui_vogais(txt)

        with open('arq_novo', 'r', encoding='utf-8') as arquivo_novo:
            txt_novo = arquivo_novo.read()
            print(f'Arquivo novo:\n{txt_novo}')

    except FileNotFoundError:
        print(f'Arquivo "{x}" não encontrado ')