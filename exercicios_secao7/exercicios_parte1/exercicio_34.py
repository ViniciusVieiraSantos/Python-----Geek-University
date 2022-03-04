"""
34) Faça um programa para ler 10 números DIFERENTES a serem armazenados
em um vetor. Os dados deverão ser armazenados no vetor na ordem que
forem sendo lidos, sendo que o caso o usuário digite um número
que já foi digitado anteriormente, o programa deverá pedir para ele
digitar outro número. Note que cada valor digitado pelo usuário deve
ser pesquisado no vetor, verificando se ele existe entre os números que
já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""
vetor = []

for i in range(1, 11):
    numero = int(input(f'Digite um numero ({i}/10): '))
    if numero in vetor:
        while numero in vetor:
            numero = int(input('Esse numero ja foi digitado,digite outro numero: '))
    vetor.append(numero)
print(f'Vetor final : {vetor}')
