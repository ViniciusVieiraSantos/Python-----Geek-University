"""
45) Faça uma função que calcule o desvio padrão de um vetor  contendo n números
Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)
onde m é a media do vetor.
"""
from random import randint


def desvio_padrao(vetor):
    somatorio = 0
    n = len(vetor)
    m = sum(vetor) / n
    for j in range(0, n):
        somatorio += (vetor[j] - m) ** 2
    desvio = (1 / (n - 1) * somatorio) ** 0.5

    return desvio


vet = []
n = int(input('Digite o tamanho da lista a ser gerada: '))

for i in range(0, n):
    valor = randint(0, 100)
    while valor in vet:
        valor = randint(0, 100)
    vet.append(valor)

print(f'Vetor gerado : {vet}')
print(f'Desvio padrão : {desvio_padrao(vet)}')
