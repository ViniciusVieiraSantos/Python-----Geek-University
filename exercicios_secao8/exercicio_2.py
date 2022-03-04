"""
2) Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a
na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir:
1 de janeiro de 2000.
"""


def data(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']

    return f'{dia} de {meses[mes]} de {ano}'


while True:
    d = int(input('Digite o dia: '))
    if d < 1 or d > 31:
        print('Dia invalido.')
    else:
        break

while True:
    m = int(input('Digite o mês: '))
    if m < 1 or m > 12:
        print('Mês invalido.')
    else:
        break

a = int(input('Digite o ano: '))

print(data(d, m, a))


