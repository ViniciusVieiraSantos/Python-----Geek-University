"""
6) Faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos
"""


def converte_segundos(horas, minutos, segundos):
    segundos += horas * 3600 + minutos * 60
    return segundos


h = int(input('Digite as horas: '))
m = int(input('Digite os minutos: '))
s = int(input('Digite os segundos: '))

print(f'Conversão para segundos : {converte_segundos(h, m, s)}')
