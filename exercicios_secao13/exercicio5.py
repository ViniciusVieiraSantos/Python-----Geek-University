"""
5) Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre
na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""


def conta_caracter(texto, caracter):
    """Retorna a quantidade de ocorrencias de um caracter em um texto,considera todos os caracter como minusculos
     Caso um dos parâmetro passados não seja uma string, retornará uma mensagem de erro.
     :param texto: O texto do arquivo que deve ser lido
     :param caracter: Caracter que será verificado o numero de ocorrencias no texto
     :return: Retorna 'quant' a quantidade de ocorrencias do caracter'.
     """
    try:
        texto = texto.lower()
        caracter = caracter.lower()
        quant = texto.count(caracter)
        return quant
    except AttributeError:
        return ' AttributeError, os parametros passados devem ser do tipo string'


if __name__ == '__main__':
    x = str(input("digite o nome do arquivo texto para ser lido: "))  # Digite 'arq' ,para ler o arquivo existente
    x += '.txt'
    try:

        with open(x, 'r', encoding='utf-8') as arquivo:
            txt = arquivo.read()
            y = str(input('Digite um caracter : '))
            print(f'Ocorrencias do caracter no arquivo :{conta_caracter(txt, y)}')

    except FileNotFoundError:
        print(f'Arquivo "{x}" não encontrado ')
