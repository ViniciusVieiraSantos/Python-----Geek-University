"""
16) Faça um programa que leia um vetor de 5 posições para números reais e,
depois, um código inteiro, Se o código for zero, finalize o programa;
se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem
inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido
"""

numeros = [float(input('Digite um numero real: ')) for i in range(5)]
print(f'Vetor : {numeros}')

while True:
    codigo = int(input('Informe um código ( 0 para parar o programa , 1 para mostrar os numeros digitados na ordem,'
                       '2 para mostrar os numeros na ordem invertida:\n'))
    if codigo == 0:
        print('Programa finalizado')
        break
    elif codigo == 1:
        print(f'Numeros na ordem direta: {sorted(numeros)}\n')
    elif codigo == 2:
        print(f'Numeros na ordem invertida: {sorted(numeros, reverse=True)}\n')
    else:
        print("Código invalido\n")
