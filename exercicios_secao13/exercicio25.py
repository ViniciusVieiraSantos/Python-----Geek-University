"""
25) Faça um programa gerenciar uma agenda de contatos. Para cada contato
armazene o nome, o telefone e o aniversário (dia e mes). O programa deve
permitir
    (a) Inserir contato
    (b) remover contato
    (c) pesquisar um contato pelo nome
    (d) listar todos os contatos
    (e) listar os contatos cujo nome inicia com uma dada letra
    (f) imprimir os aniversariantes do mês
Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados
com os dados contidos neste arquivo binário.
"""
from datetime import date


def inserir_contato():
    nome = str(input('\nNome: ')).title().strip()
    numero = str(input('Numero: '))

    while True:
        dia = str(input('Dia do aniversario: ')).strip()
        if 0 < int(dia) < 32:
            break
        print("Dia invalido!")
    while True:
        mes = str(input('Mês do aniversario: ')).strip()
        if 0 < int(mes) < 13:
            break
        print("Mês invalido!")

    ani = dia + '/' + mes
    agenda[nome] = [numero, ani]
    str(input(f'Contato " {nome} " salvo com sucesso.Digite qualquer coisa para continuar: '))


def remover_contato():
    if not agenda:
        print('\nNão possui contato salvo.')
    else:
        print('\nContatos salvos:')
        for nome in agenda:
            print(nome, end="  |  ")
        print('\n')
        while True:
            n = str(input('Digite o nome a ser removido (digite "0" para sair): ')).title().strip()
            if n == '0':
                break
            if n not in agenda.keys():
                print(f"O nome {n} não está registrado na agenda.")

            else:
                agenda.pop(n)
                str(input(f'Contato " {n} " removido com sucesso.Digite qualquer coisa para continuar: '))
                break


def pesquisar_nome():
    while True:
        if not agenda:
            print('\nNão possui contato salvo.')
            break
        n = str(input('Digite um nome: ')).title()
        print()
        contatos = [nome for nome in agenda if n in nome.split()]
        if len(contatos) == 0:
            print(f'" {n} "Não foi encontrado na agenda.')
        else:
            print('Contatos encontrados:')
            [print(f'{nome}{" " * (30 - len(nome))}  Numero: {agenda[nome][0]}  '
                   f'Aniversario: {agenda[nome][1]}') for nome in contatos]
        s = str(input('Digite qualquer coisa para continuar ou "0" para sair: '))
        if s == '0':
            break


def listar_contatos():
    if not agenda:
        print('\nNão possui contato salvo.')
        return None
    print('Contatos salvos:\n')
    [print(f'{nome}{" " * (30 - len(nome))}  Numero: {agenda[nome][0]}  '
           f'Aniversario: {agenda[nome][1]}') for nome in agenda]
    str(input('\nDigite qualquer coisa para continuar: '))


def listar_letras():
    while True:
        if not agenda:
            print('\nNão possui contato salvo.')
            return None
        letra = str(input('Digite uma letra: ')).upper()[0]
        print()
        contatos = [nome for nome in agenda if letra == nome[0]]
        if len(contatos) == 0:
            print(f'Não foi encontrado na agenda um nome que começa com a letra "{letra}".')
        else:
            print('Contatos encontrados: ')
            [print(f'{nome} :\nNumero: {agenda[nome][0]}   '
                   f'Aniversario: {agenda[nome][1]}\n') for nome in contatos]
        s = str(input('Digite qualquer coisa para continuar ou "0" para sair: '))
        if s == '0':
            break


def aniversariantes():

    if not agenda:
        print('\nNão possui contato salvo.')
        return None
    else:
        aniversariante = [nome for nome in agenda if mes_atual in agenda[nome][1].split('/')[1]]
    if len(aniversariante) > 0:
        print('Aniversariantes do mês:')
        [print(f'{nome}{" " * (30 - len(nome))} Aniversario: {agenda[nome][1]}') for nome in aniversariante]
    else:
        print('\nNão possui contatos que fazem aniversario neste mês.')
    str(input('Digite qualquer coisa para sair: '))


agenda = {}
mes_atual = str(date.today().month)


try:
    with open('agenda.bin', 'rb') as arquivo:
        txt = arquivo.read().decode("utf8").strip().split('\n')
        for linha in txt:
            dados_contato = linha.split(':')
            agenda[dados_contato[0].strip()] = [dados_contato[1], dados_contato[2]]
except FileNotFoundError:
    print("Arquivo 'despensa.bin' não existe.")
except IndexError:
    print('Lista existe mas está vazia.')


while True:
    x = str(input('\nAgenda:\n  0 - Sair.\n  1 - Inserir contato.\n  2 - Remover contato.\n  '
                  '3 - Pesquisar um contato pelo nome.\n  4 - Listar todos os contatos.\n  '
                  '5 - Listar os contatos cujo nome inicia com uma dada letra\n  '
                  '6 - Imprimir os aniversariantes do mês\nEscolha uma opção: '))
    if x == '0':
        # Colocar escrever aqui
        break
    if x == '1':
        print(f'\nOpção "1" escolhida, inserir contato:')
        inserir_contato()
    if x == '2':
        print(f'\nOpção "2" escolhida, remover contato:')
        remover_contato()
    if x == '3':
        print(f'\nOpção "3" escolhida, pesquisar contato pelo nome:')
        pesquisar_nome()
    if x == '4':
        print(f'\nOpção "4" escolhida, listar todos os contatos:')
        listar_contatos()
    if x == '5':
        print(f'\nOpção "5" escolhida, pesquisar contato pela letra:')
        listar_letras()
    if x == '6':
        print(f'\nOpção "6" escolhida, imprimir os aniversariantes do mês:')
        aniversariantes()

try:
    with open('agenda.bin', 'wb') as arquivo:
        for contato in agenda:
            arquivo.write(f'{contato} : {agenda[contato][0]} : {agenda[contato][1]}\n'.encode("utf8"))
except FileNotFoundError:
    print("O programa não possui permissão para criar um diretorio/pasta!")
