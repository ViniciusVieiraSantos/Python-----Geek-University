"""
17) Faça um programa que leia um arquivo que contenha as dimensões de uma
matrix (linha e coluna), a quantidade de posições que serão anuladas, e as
posições a serem anuladas (linha e coluna). O programa lê esse arquivo e,
em seguida, produz um novo arquivo com a matriz com as dimensões dadas
no arquivo lido, e todas as posições especificadas no arquivo ZERADAS e o
restante recebendo o valor 1.
Ex: arquivo "matriz.txt"
3 3 2 /*3 e 3 dimensões da matriz e 2 posições que serão anuladas*/
1 0
1 2   /*Posições da matriz que serão anuladas.
arquivo "matriz_saida.txt"
saida:
1 1 1
0 1 0
1 1 1
"""
"""
linha 1 dimensões da matriz e qtd de posições a serem anuladas
linha 2..n posições a serem anunladas
"""


def escreve_matriz(posicoes_anular, linha, colunas):
    string_linha = ""
    for posicao in posicoes_anular:
        posicao_int = [int(posicao[0]), int(posicao[1])]
        print(linha, posicao_int[0])

        if linha == posicao_int[0]:
            for coluna in range(colunas):
                if coluna == posicao_int[1]:
                    string_linha += '0 '
                else:
                    string_linha += '1 '
            return string_linha

    else:
        return '1 ' * colunas


try:
    with open('matriz.txt', 'r') as arquivo, open('matriz_saida.txt', 'w') as saida:
        linhas = arquivo.read().split('\n')
        linhas = [linha.split() for linha in linhas]

        # Ler as dimensoes da matriz e numero de pontos a serem anulados
        num_linha, num_coluna, anular_posicoes = int(linhas[0][0]), int(linhas[0][1]), int(linhas[0][2])

        # Pegar todas as posicoes a serem anuladas desde a linha 2 (linha[1])
        # até a quantidade definida pela variavel 'anular_posicoes' +1
        posicoes = [linhas[i] for i in range(1, anular_posicoes + 1)]

        for linha in range(0, num_linha):  # Escrever linha por linha da matriz no novo arquivo
            saida.write(f'{escreve_matriz(posicoes, linha, num_coluna)}\n'
                        f'')


except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
