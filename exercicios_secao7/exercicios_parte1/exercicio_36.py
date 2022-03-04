"""
36) Leia um vetor com 10 números reais, ordene os elementos deste valor,
e no final escreva os elementos do vetor ordenado.
"""


lista = [float(input(f"Digite um número real ({i}/10): ")) for i in range(1, 11)]
lista.sort()

print(f"\nVetor ordenada: {lista}")
