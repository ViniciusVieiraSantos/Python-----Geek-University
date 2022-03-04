"""
25) Faça um programa que preencha um vetor de tamanho 100
com os 100 primeiros naturais que não são múltiplos de 7 ou
que terminam com 7.
"""

numeros = []
i = 0
while len(numeros) < 100:
    if (not(i % 7 == 0)) and not(str(i)[-1] == '7'):
        numeros.append(i)
    i += 1
print(numeros)
