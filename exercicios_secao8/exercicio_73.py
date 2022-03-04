"""
73) Foi realizada uma pesquisa de algumas características físicas de cinco
habitantes de certa região. De cada habitante foram coletados os seguintes
dados: sexo, cor dos olhos (A - Azuis ou C - Castanhos), cor dos cabelos
(L - Louros, P - Pretos ou C - Castanhos) e idade
    . Faça uma função que leia esses dados em um vetor
    . Faça uma função que determine a média de idade das pessoas
    com olhos castanhos e cabelos pretos
    . Faça uma função que determine e devolva ao programa principal a maior
    idade entre os habitantes
    . Faça uma função que determine e devolva ao programa principal a quantidade
    de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que
    tenham olhos azuis e cabelos louros
"""


def ler_dados(dados):
    for i in range(5):
        print(f'Dados habitante {i+1} :')

        x = input('Sexo(M / F): ').upper()
        while x != 'M' and x != 'F':
            x = str(input('Entrada invalida,digite "M" para masculino ou "F" para feminino: ')).upper()

        y = input('Cor dos olhos "A" - azuis, "C" - castanhos: ').upper()
        while y != 'A' and y != 'C':
            y = str(input('Entrada invalida,digite "A" para azuis ou "C" para castanhos: ')).upper()

        z = input('Cor dos cabelos "L" - louros, "P" - pretos, "C" - castanhos: ').upper()
        while z != 'L' and z != 'P' and z != 'C':
            z = str(input('Entrada invalida,digite "L" - louros, "P" - pretos, "C" - castanhos: ')).upper()

        w = int(input('Digite a idade:'))
        while w < 0:
            w = str(input('Entrada invalida,digite a idade: ')).upper()

        dic = {'Sexo': x, 'Olhos': y, 'Cabelo': z, 'Idade': w}
        dados.append(dic)
        print()

    return dados


def media_idade(dados):
    soma_idade = 0
    cont = 0
    for i in range(len(dados)):

        if dados[i]['Olhos'] == 'C' and dados[i]['Cabelo'] == 'P':
            soma_idade += dados[i]['Idade']
            cont += 1

    if cont == 0:
        return ' Nenhuma pessoa possui olhos castanhos e cabelo preto'

    return int(soma_idade/cont)


def maior_idade(dados):
    maior = 0
    for i in range(len(dados)):
        if dados[i]['Idade'] > maior:
            maior = dados[i]['Idade']
    return maior


def quantidade_feminino(dados):
    cont = 0
    for i in range(len(dados)):

        if dados[i]['Sexo'] == 'F' and 18 <= dados[i]['Idade'] <= 35 and dados[i]['Olhos'] == 'A' \
                and dados[i]['Cabelo'] == 'L':
            cont += 1

    if cont == 0:
        return ' Nenhum habitante possui essas caracteristicas'

    return cont


d = []
d = ler_dados(d)
print(f'Média da idade das pessoas com olhos castanhos e cabelo preto : {media_idade(d)} anos')
print(f'A maior idade entre os habitantes : {maior_idade(d)} anos')
print(f'Quantidade de mulheres entre 18 e 35 anos que possuem olhos azuis e cabelo loiro : {quantidade_feminino(d)}')
