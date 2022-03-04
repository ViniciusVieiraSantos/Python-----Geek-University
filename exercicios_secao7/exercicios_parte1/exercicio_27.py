"""
27) Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os
elementos que são primos e suas respectivas posições no vetor.
"""

lista = [int(input("Digite um número: ")) for i in range(10)]

for i in lista:
    cont = 0

    for j in range(1, i+1):
        if i % j == 0:
            cont += 1

    if cont <= 2:
        print(f"Elementos que são primos e suas respectivas posições no vetor: elemento = {i} -> "
              f"posição = {lista.index(i)}")
