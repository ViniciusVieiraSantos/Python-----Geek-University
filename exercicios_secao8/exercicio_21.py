"""
21) Escreva uma função para determinar a quantidade de números
primos abaixo de N.
"""


def primos_abaixo(numero):
    quantidade = 0
    if numero > 2:
        for i in range(2, numero):
            cont = 0
            for j in range(1, i+1):
                if i % j == 0:
                    cont += 1
                    if cont > 2:
                        break
            if cont == 2:
                quantidade += 1
    return quantidade


x = int(input('Digite um numero: '))
print(f'Quantidade de numeros primos abaixo de {x} : {primos_abaixo(x)}')
