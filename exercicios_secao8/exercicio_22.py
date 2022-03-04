"""
22) Crie uma função que receba parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):
    !
    !!
    !!!
    !!!!
    !!!!!
"""


def gerar_linhas(numero):
    print()
    if numero > 0:
        for i in range(1, numero+1):
            print('!' * i)
        return '!' * numero


x = int(input('Digite um numero: '))
gerar_linhas(x)
