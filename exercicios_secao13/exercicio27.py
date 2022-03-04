"""
27) Faça um programa para gerenciar as notas dos alunos de uma turma
salva em um arquivo. O programa deverá ter um menu contendo as seguinte opções:
    (a) Definir informações da turma;
    (b) Inserir aluno e notas;
    (c) Exibir alunos e médias;
    (d) Exibir alunos aprovados;
    (e) Exibir alunos reprovados;
    (f) Salvar dados em Disco;
    (g) Sair do programa (fim)
Faça a rotina que gerencia o menu dentro do main, e para cada uma das
opções deste menu, crie uma função específica

"""


def inserir():
    print(f'\nInserir nota:')
    nome = str(input('Nome do aluno: ')).title()
    n1 = float(input('Nota 1 do aluno: '))
    n2 = float(input('Nota 2 do aluno: '))
    alunos[nome] = [n1, n2]


def alunos_medias():
    print(f'\nMedia alunos:')
    for aluno in alunos:
        media = sum(alunos[aluno])/ 2
        print(f'{aluno} : Média = {media}')


def alunos_aprovados():
    aprovados = False
    print(f'\nAlunos aprovados:')
    for aluno in alunos:
        media = sum(alunos[aluno]) / 2
        if media >= 7:
            print(aluno)
            aprovados = True
    if not aprovados:
        print('Nenhum aluno foi aprovado')


def alunos_reprovados():
    reprovados = False
    print(f'\nAlunos reprovados:')
    for aluno in alunos:
        media = sum(alunos[aluno]) / 2
        if media < 7:
            print(aluno)
            reprovados = True
    if not reprovados:
        print('Nenhum aluno foi reprovado')


def salvar():
    with open('turma.txt', 'w', encoding='utf-8') as arquivo:
        for aluno in alunos:
            arquivo.write(f'{aluno}/{alunos[aluno][0]}/{alunos[aluno][1]}\n')
    print('\nDados salvos com sucesso.')


alunos = {}

try:
    with open('turma.txt', 'r', encoding='utf-8') as leitura:
        linhas = leitura.readlines()
        for linha in linhas:
            if linha != '\n':
                dados = linha.split('/')
                alunos[dados[0]] = [float(dados[1]), float(dados[2])]
except FileNotFoundError:
    print('Arquivo não encontrado')


while True:
    o = str(input('\nMenu:\n  0 - Sair.\n  1 - Inserir notas.\n  2 - Exibir médias.\n  '
                  '3 - Exibir alunos aprovados.\n  4 - Exibir alunos reprovados.\n  '
                  '5 - Salvar dados.\nEscolha uma opção: '))
    if o == '0':
        break
    if o == '1':
        inserir()
        input('\nDigite qualquer coisa para continuar: ')
    if o == '2':
        alunos_medias()
        input('\nDigite qualquer coisa para continuar: ')
    if o == '3':
        alunos_aprovados()
        input('\nDigite qualquer coisa para continuar: ')
    if o == '4':
        alunos_reprovados()
        input('\nDigite qualquer coisa para continuar: ')
    if o == '5':
        salvar()
        input('\nDigite qualquer coisa para continuar: ')