"""
23) Ler dois conjuntos de números reais, armazenando-os em vetores
e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos
cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por: x1 * y1 + x2 * y2 + ... + xn * yn
"""
from random import uniform

conjunto_1 = [round(uniform(1, 20), 1) for i in range(5)]
conjunto_2 = [round(uniform(1, 20), 1) for j in range(5)]
print(f'\nConjunto 1 : {conjunto_1}\nConjunto 2 : {conjunto_2}')

produto_escalar = [round(conjunto_1[i] * conjunto_2[i], 1) for i in range(5)]
print(f'Produto escalar : {produto_escalar}')
