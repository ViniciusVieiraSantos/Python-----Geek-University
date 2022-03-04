"""
9) Crie um programa que lê 6 valores inteiros pares , em seguida, mostre
na tela os valores lidos na ordem inversa
"""
vetor = []
for i in range(6):
    x = int(input(f'Digite um numero inteiro par ({i+1}/6) : '))
    while x % 2 != 0:
        x = int(input(f'O numero digitado é impar,digite um numero inteiro par ({i+1}/6) : '))
    vetor.append(x)
print(f'Vetor : {vetor}')
vetor_inverso = [vetor[j] for j in range(5, -1, -1)]
print(f'Vetor inverso : {vetor_inverso}')
