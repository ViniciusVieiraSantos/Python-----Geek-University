"""
37) Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 >
A7 > A8 > ... > A11, ou seja, está ordenando em ordem crescente até
o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente.
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os
elementos.
"""
lista = [float(input(f"Digite um número real ({i}/11): ")) for i in range(1, 12)]
lista.sort()

print(f"\nVetor ordenado: {lista}")

vetor_a = [lista[i] if i < 6 else lista[5 - i] for i in range(0, 11)]

print(f'Vetor A : {vetor_a}')
