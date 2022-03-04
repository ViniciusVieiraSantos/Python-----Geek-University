"""
35) Faça um programa que leia dois números a e b (positivos menores
que 10000) e:
    . Crie um vetor onde cada posição é um algorismo do número. A primeira
    posição é o algarismo menos significativo;
    . Crie um vetor que seja a soma de a e b, mas faça faça-o usando
    apenas os vetores construídos anteriormente.
Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia
10 do resultado e some 1 à próxima posição.
"""

num_a = int(input('Digite um numero positivo menor que 10000: '))
while num_a < 0 or num_a > 10000:
    num_a = int(input('Numero invalido,digite um numero positivo menor que 10000: '))

vetor_1 = list(str(num_a))[::-1]       # Transformar os numeros digitidos em string e inverter-los

num_b = int(input('Digite outro numero positivo menor que 10000: '))
while num_b < 0 or num_b > 10000:
    num_b = int(input('Numero invalido,digite um numero positivo menor que 10000: '))

vetor_2 = list(str(num_b))[::-1]       # Transformar os numeros digitidos em string e inverter-los

# Transformar os valores do vetor em int
vetor_1 = [int(vetor_1[i]) for i in range(len(vetor_1))]
vetor_2 = [int(vetor_2[i]) for i in range(len(vetor_2))]

# Garantir que os vetores tenham o mesmo tamanho:
if len(vetor_1) != len(vetor_2):
    while len(vetor_1) < len(vetor_2):
        vetor_1.append(0)
    while len(vetor_2) < len(vetor_1):
        vetor_2.append(0)

vetor_soma = [0] * len(vetor_1)

# soma
for i in range(len(vetor_1)):
    soma = vetor_1[i] + vetor_2[i]

    if soma > 10:
        soma -= 10
        if i == len(vetor_1)-1:
            vetor_soma.append(0)
        vetor_soma[i+1] = 1

    vetor_soma[i] += soma

# imprimir vetores:
print(f'Vetor 1 : {vetor_1}\nVetor 2: {vetor_2}')
print(f'Vetor soma : {vetor_soma}')
