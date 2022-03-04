"""
22) Faça um programa que recebe como entrada o nome de um arquivo de
entrada e o nome de um arquivo saída. O arquivo de entrada contém
o nome de um aluno ocupando 40 caracteres e três inteiros que indicam
suas notas. O programa deverá ler o arquivo de entrada e gerar um arquivo
de saída onde aparece o nome do aluno e as suas notas em ordem crescente.
"""

# Utilizar 'aluno_notas.txt' para arquivo de entrada
arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome (caso o arquivo esteja "
                            "no mesmo local do programa): "))
arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada+".txt"

# Utilizar 'aluno_notas_saida.txt' para arquivo de saida
arquivo_saida = str(input("Digite o caminho do arquivo de saida ou o seu nome  (caso o arquivo esteja no mesmo local "
                          "do programa): "))
arquivo_saida = arquivo_saida if ".txt" in arquivo_saida else arquivo_saida+".txt"



try:
    with open(arquivo_entrada, 'r', encoding='utf-8') as arq_entrada, \
            open(arquivo_saida, 'w', encoding='utf-8') as arq_saida:
        linha = arq_entrada.readline().split()
        nome = ' '.join(linha[0:len(linha)-3])

        notas = sorted(linha[-1:-4:-1], key=int)

        arq_saida.write(nome + ' Notas: ' + notas[0]+' ' + notas[1]+' ' + notas[2])

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")