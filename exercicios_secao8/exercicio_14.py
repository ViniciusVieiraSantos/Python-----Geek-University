"""
14) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    | CONSUMO    | (km/l)  | MENSAGEM
    | menor que  |   8     | Venda o carro!
    | entre      | 8 e 12  | Econômico
    | maior que  |  12     | Super econômico!
"""


def consumo_carro(kilometros, litros):
    consumo = kilometros / litros
    if consumo < 8:
        return 'Venda o carro!'
    elif (consumo >= 8) and (consumo <= 14):
        return 'Econômico!'
    return 'Super economico'


a = int(input("Digite o numero de kilometros percorrido pelo carro: "))
b = int(input("Digite o numero de litros consumidos: "))

print(consumo_carro(a, b))
