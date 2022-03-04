"""
26) Faça um programa que calcule o desvio padrão de um vetor
v contendo n = 10 números, onde m é a média do vetor.
    Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)
"""
# RECEBENDO OS VALORES
v = []
n = 8
soma = 0
variancia = 0
for i in range(n):
    v.append(int(input(f'Digite o {i + 1}º valor: ')))
    soma += v[i]

# MÉDIA ARITIMÉTICA
m = soma / n

# VARIÂNCIA AMOSTRAL
for j in v:
    variancia += (j - m) ** 2
s = variancia / (n - 1)

# DESVIO PADRÃO AMOSTRAL
d = s ** 0.5
print(f'Desvio padrão amostral : {d}')
