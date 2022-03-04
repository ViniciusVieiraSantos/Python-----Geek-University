"""
6) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
"""


def conta_letras(texto):
    """
    Conta quantas vezes cada letra do alfabeto aparece no texto.
    Caso o que for passado por parâmetro não seja uma string, retornará uma mensagem de erro.
    :param texto: O texto em que sera contado o numero de letras
    :return: Retorna um dicionario com cada letra do alfabeto como key e como value o numero de vezes
             que esse letra aparece no texto
    """
    try:
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
                    , 'u', 'v', 'w', 'x', 'y', 'z']
        texto = texto.lower()
        dict_ocorrencias = {}
        for letra in alfabeto:
            dict_ocorrencias[letra] = texto.count(letra)
        return dict_ocorrencias

    except AttributeError:
        return ' AttributeError, o parametro passado deve ser uma string'


if __name__ == '__main__':
    x = str(input("\nDigite o nome do arquivo texto para ser lido: "))   # Digite 'arq' ,para ler o arquivo existente
    x += '.txt'
    try:

        with open(x, 'r', encoding='utf-8') as arquivo:
            txt = arquivo.read()
            print(f'Numero de letras no texto:\n{conta_letras(txt)}')

    except FileNotFoundError:
        print(f'Arquivo "{x}" não encontrado ')
