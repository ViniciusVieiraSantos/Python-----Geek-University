"""
15) Crie um programa que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:
(a) Determimnar se eles lados formam um triângulo, sabendo que:
    . O comprimento de cada lado de um triângulo é menor do que a soma dos outros
    dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um
triângulo. Sendo que:
    . Chama-se equilátero o triângulo que tem três lados iguais.
    . Denominam-se isósceles o triângulo que tem o comprimento
    de dois lados iguais
    . Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""


def determina_triangulo(lado_1, lado_2, lado_3):
    if (lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2):
        return tipo_triangulo(lado_1, lado_2, lado_3)
    return 'Não é um triangulo!'


def tipo_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 == lado_3:
        return 'É um triângulo Equilatero'
    elif (lado_1 == lado_2) or (lado_2 == lado_3) or (lado_3 == lado_1):
        return 'É um triângulo Isósceles'
    elif lado_1 != lado_2 != lado_3:
        return 'É um triângulo Escaleno'


lados = []

print('Digite 3 valores maiores que zero :')
for i in range(3):
    valor = int(input())
    while valor < 1:
        valor = int(input('Valor invalido! Digite um numero maior que 0 :\n'))
    print("Digite outro valor maior que zero:")
    lados.append(valor)

print(determina_triangulo(*lados))
