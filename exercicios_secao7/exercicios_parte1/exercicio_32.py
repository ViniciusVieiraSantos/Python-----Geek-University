"""
32) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma
que o usuário não informa elementos repetidos). Calcule e mostre os
vetores resultantes em cada caso abaixo:
    . Soma entre x e y: soma de cada elemento x com o elemento da mesma
    posição em y.
    . Produto entre x e y: multiplicação de cada elemento de x com o
    elemento da mesma posição em y.
    . Diferença entre x e y: todos os elementos de x que não existam em y.
    . Interseção entre x e y: apenas os elementos que aparecem nos dois vetores
    . União entre x e y: todos os elemntos de x, e todos os elementos de y
    que não estão em x.
"""

vetor_x = [int(input(f'Digite um numero para o vetor x ({i}/5): ')) for i in range(1, 6)]
vetor_y = [int(input(f'Digite um numero para o vetor y ({j}/5): ')) for j in range(1, 6)]
print(f'\nVetor x : {vetor_x}    Vetor y: {vetor_y}\n')
soma = [vetor_x[i] + vetor_y[i] for i in range(len(vetor_x))]
mult = [vetor_x[i] * vetor_y[i] for i in range(len(vetor_x))]
dif = [vetor_x[i] - vetor_y[i] for i in range(len(vetor_x))]
vetor_x = set(vetor_x)
vetor_y = set(vetor_y)
inter = vetor_x.intersection(vetor_y)
uni = vetor_x.union(vetor_y)

print(f'Soma dos elementos dos vetores x e y: {soma}\nMultiplicação dos elementos dos vetores  x e y: {mult}\n'
      f'Diferença dos elementos dos vetores x e y: {dif}\nIntersecção entre x e y: '
      f'{inter}\nUnião entre x e y: {uni}')
