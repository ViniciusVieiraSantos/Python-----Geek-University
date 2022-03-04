"""
3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""

vetor_1 = [float(input('Digite um numero: ')) for i in range(10)]
vetor_2 = [vetor_1[j] ** 2 for j in range(10)]
print(f'Vetor 1 : {vetor_1}    Vetor 2 : {vetor_2}')
