"""
26) Crue um programa que declare uma classe para o cadastro de alunos.
    (a) Deverão ser armazenados, para cada aluno: matrícula, sobrenome (apenas um),
    e ano de nascimento.
    (b) Ao início do programa, o usuário deverá informar o número de alunos que
    serão armazenados
    (c) O programa deverá pedir ao usuário que entre com as informações dos alunos.
    (d) Em seguida, essas informações deverão ser gravadas em um arquivo
"""
matricula = 0
ultima_linha = 0

try:
    with open('classe.txt', 'a', encoding='utf-8') as adicionar:

        with open('classe.txt', 'r', encoding='utf-8') as leitura:
            arquivo = leitura.readlines()
            for linhas in arquivo:
                if linhas.strip():
                    ultima_linha = linhas
            if ultima_linha != 0:
                matricula = int(ultima_linha.split('/')[0])

        i = 0
        n = int(input('Numeros de alunos á serem cadastrados: '))
        while i < n:
            matricula += 1
            print('Insira os dados do aluno :')
            s = str(input('Sobrenome: ')).split()[0].title()
            ano = int(input('Ano de nascimento: '))
            adicionar.write(f'{matricula}/{s}/{ano}\n')
            i += 1
except ValueError:
    print('Erro')
