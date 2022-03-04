"""
4) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais e quantas são consoantes
"""


def conta_vogais(texto):
    """
    Conta a quantidade de vogais que existem no texto recebido por parâmetro.
    Caso o que for passado por parâmetro não seja uma string, retornará uma mensagem de erro
    :param texto: O texto em que sera contado o numero de vogais
    :return: Retorna 'quant' ,que contem a quantidade de vogais'.
    """
    try:
        vogais = ['a', 'e', 'i', 'o', 'u']
        texto = texto.lower()
        quant = 0
        for vogal in vogais:
            quant += texto.count(vogal)
        return quant
    except AttributeError:
        return ' AttributeError, o parametro passado deve ser uma string'


def conta_consoantes(texto):
    """Conta a quantidade de consoantes que existem no texto recebido por parâmetro.
     Caso o que for passado por parâmetro não seja uma string, retornará uma mensagem de erro
     :param texto: O texto em que sera contado o numero de consoantes
     :return: Retorna 'quant' ,que contem a quantidade de consoantes'.
     """
    try:
        consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                      'y', 'z']
        texto = texto.lower()
        quant = 0
        for consoante in consoantes:
            quant += texto.count(consoante)
        return quant
    except AttributeError:
        return ' AttributeError, o parametro passado deve ser uma string'


if __name__ == '__main__':
    x = input("digite o nome do arquivo texto para ser lido: ")
    x += '.txt'
    try:

        with open(x, 'r', encoding='utf-8') as arquivo:
            txt = arquivo.read()
            print(f'Quantidade de vogais no arquivo : {conta_vogais(txt)}')
            print(f'Quantidade de consoantes no arquivo : {conta_consoantes(txt)}')

    except FileNotFoundError:
        print(f'Arquivo "{x}" não encontrado ')



