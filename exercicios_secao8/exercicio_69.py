"""
69) Faça um programa que faça operações simples de frações:
    . Crie e leia duas frações p e q, compostas por numerador e denominador.
    . Encontre o máximo divisor comum entre o numerador e o denominador, e simplifique
    as frações.
    . Apresente a soma, a subtração, o produto e o quociente entre as frações lidas.
Obs.: Cria uma função para cada item.
"""


def criar_fracoes():
    p = []
    q = []
    p.append(int((input('Digite o numerador da fração "p" : '))))
    p.append(int((input('Digite o denominador da fração "p" : '))))
    q.append(int((input('Digite o numerador da fração "q" : '))))
    q.append(int((input('Digite o denominador da fração "q" : '))))
    p[0], p[1], mdc = simplifica_fracao(p[0], p[1])
    print(f'Mdc : {mdc}  Fração 1 simplificada : {p[0]}/{p[1]}')
    q[0], q[1], mdc = simplifica_fracao(q[0], q[1])
    print(f'Mdc : {mdc}  Fração 2 simplificada : {q[0]}/{q[1]}')
    operacoes_fracoes(p[0], p[1], q[0], q[1])


def simplifica_fracao(numerador, denominador):
    for mdc in range(denominador, 0, -1):
        if numerador % mdc == 0 and denominador % mdc == 0:
            return int(numerador / mdc), int(denominador / mdc), mdc


def operacoes_fracoes(numerador_1, denominador_1, numerador_2, denominador_2):
    divisor = 2
    mmc = 1
    if denominador_1 == denominador_2:
        mmc = denominador_1
        numerador_soma = numerador_1 + numerador_2
        numerador_sub = numerador_1 + numerador_2

    else:
        den_1, den_2 = denominador_1, denominador_2
        while max(den_1, den_2) != 1:
            if den_1 % divisor == 0 and den_2 % divisor == 0:
                den_1 /= divisor
                den_2 /= divisor
                mmc *= divisor

            elif den_1 % divisor == 0 and den_2 % divisor != 0:
                den_1 /= divisor
                mmc *= divisor

            elif den_1 % divisor != 0 and den_2 % divisor == 0:
                den_2 /= divisor
                mmc *= divisor

            elif den_1 % divisor != 0 and den_2 % divisor != 0:
                divisor += 1
        numerador_soma = numerador_1 * (mmc / denominador_1) + numerador_2 * (mmc / denominador_2)
        numerador_sub = numerador_1 * (mmc / denominador_1) - numerador_2 * (mmc / denominador_2)

    numerador_soma, mmc = simplifica_fracao(numerador_soma, mmc)[0:2]
    print(f'Soma frações :{numerador_soma}/{mmc}')

    numerador_sub, mmc = simplifica_fracao(numerador_sub, mmc)[0:2]
    print(f'Subtração frações :{numerador_sub}/{mmc}')

    num_produto = numerador_1 * numerador_2
    den_produto = denominador_1 * denominador_2
    den_produto, num_produto = simplifica_fracao(den_produto, num_produto)[0:2]
    print(f'Produto das frações: {num_produto}/{den_produto}')

    num_divisao = numerador_1 * denominador_2
    den_divisao = denominador_1 * numerador_2
    den_divisao, num_divisao = simplifica_fracao(den_divisao, num_divisao)[0:2]
    print(f'Divisao entre as frações: {num_divisao}/{den_divisao}')


criar_fracoes()
