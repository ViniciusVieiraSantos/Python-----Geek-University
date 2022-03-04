"""
29) Codifique um programa que manipule um arquivo contendo registros
descritos pelos seguntes campos: codigo_vendedor, nome_vendedor,
valor_da_venda e mes. A manipulação do arquivo em questão é feita
através da execução das operações disonibilizadas pelo seguinte menu:
    . Criar o arquivo de dados;
    . Incluir um determinado registro no arquivo;
    . Excluir um determinado vendedor no arquivo;
    . Alterar o valor de uma venda no arquivo;
    . Imprimir os registros na saída padrão;
    . Excluir o arquivo de dados;
    . Finalizar o programa.
Os registros devem estar ordenados no arquivo, de forma crescente, de acordo
com as informações contidas nos campos codigo_vendedor e mes. Não deve existir
mais de um registros no arquivo com mesmos valores nos campos codigo_vendedor e mes.

"""
import os


def incluir_registro():
    dados = []
    print('\n|Incluir registro|')
    codigo = str(input('Codigo do vendedor: '))

    if codigo not in registros:  # Se o codigo do funcionario não existir, será cadastrado um novo funcionario
        nome = str(input('Nome do vendedor: ')).title()
        dados.append(nome)

    else:
        dados = registros[codigo]  # Se existir, a variavel dados recebera todos os registros salvos do funcionario
        print(f'Nome do vendedor: {registros[codigo][0]}')

    mes = int(input('Digite o mês da venda: '))
    mes_salvo = True
    while mes_salvo:
        if 0 < mes <= 12:
            if len(dados) > 1:
                # dados = [nome, [valor, mes]....] /// dados[0] = nome ///dados [1]..dados[x].. = [valor,mes]
                for i in range(1, len(dados)):
                    if mes == dados[i][1]:  # dados [i][0] == valor   dados[i][1] == mes
                        mes = int(input(f"Já existe um registro de venda no mês {mes}."
                                        " Digite outro mês ou 0 para sair: "))
                        break
                    if i == len(dados) - 1:  # Se o loop 'for' chegar aqui é por que o mes não esta salvo nos registros
                        mes_salvo = False
            else:
                mes_salvo = False
        elif mes == 0:
            return
        else:
            mes = int(input(f"'Mês invalido!'.Digite outro mês ou 0 para sair: "))

    valor = float(input('Valor da venda: '))
    dados.append([valor, mes])
    registros[codigo] = dados
    escrever_arquivo()


def excluir_vendedor():
    print('\n|Excluir vendedor|')
    if not registros:
        print('\nO arquivo não possui registro salvo.')
    else:
        print('Vendedores cadastrados:')
        print(f'Codigo | Nome')
        [print(f' {codigo:^6}|{registros[codigo][0]}') for codigo in registros]

        while True:
            cod = str(input('\nDigite o codigo do vendedor á ser removido (0 para sair): '))
            if cod == '0':
                break
            elif cod not in registros:
                print(f'\nO código {cod} não esta registrado.')
            else:
                del registros[cod]
                escrever_arquivo()


def alterar_valor():
    print('\n|Alterar valor de venda|')
    if not registros:
        print('\nO arquivo não possui registro salvo.')
    else:
        print('Vendedores cadastrados:')
        print(f'Codigo | Nome')
        [print(f' {codigo:^6}|{registros[codigo][0]}') for codigo in registros]
        while True:
            cod = str(input('\nDigite o codigo do vendedor que realizou a venda (0 para sair): '))
            if cod == '0':
                break
            elif cod not in registros:
                print(f'O código {cod} não esta registrado.')
            else:
                while True:
                    mes = int(input('\nDigite o mês da venda: '))
                    if (mes < 1) or (mes > 12):
                        print('Mês invalido!\n')
                    else:
                        alterado = False
                        for i in range(1, len(registros[cod])):
                            if mes == registros[cod][i][1]:

                                valor = float(input('Informe o novo valor da venda: '))
                                registros[cod][i][0] = valor
                                alterado = True
                                escrever_arquivo()
                                break
                        if alterado:
                            break
                        print(f'O mês {mes} não possui registro de venda.')


def imprimir_registro():
    print('\n|Imprimir Registros|')
    ler_arquivo()
    if not registros:
        print('\nO arquivo não possui registro salvo.')
    else:
        print(f'Codigo | Nome{" "*25}| Mês | Valor')
        [[print(f' {codigo:^6}|{registros[codigo][0]:<30}|{registros[codigo][i][1]:^5}|'
                f'{registros[codigo][i][0]:>10} R$') for i in range(1, len(registros[codigo]))] for codigo in registros]


def escrever_arquivo():
    try:
        with open('vendas.txt', 'w', encoding='utf-8') as arquivo:
            for key in sorted(registros):  # For das chaves ordernadas do dicionario
                arquivo.write(f'{key}|{registros[key][0]}')
                dados = registros[key].copy()
                dados.pop(0)  # remover o nome para poder ordernar os meses
                dados.sort(key=lambda x: x[1])   #ordernar os meses
                [arquivo.write(f'|{dado}') for dado in dados]
                arquivo.write('|\n')

    except:
        print()


def ler_arquivo():
    try:
        with open('vendas.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.split('|')
                dados.pop()
                codigo = dados.pop(0)
                nome = dados.pop(0)
                lista = [nome]
                for i in range(len(dados)):
                    d = dados[i].replace('[', '').replace(']', '').split(", ")
                    lista.append([float(d[0]), int(d[1])])
                registros[f'{codigo}'] = lista
    except FileNotFoundError:
        print()


def excluir_arquivo():
    print('\n|Excluir Arquivo|')
    try:
        local_arq = f'{os.path.dirname(os.path.realpath(__file__))}/vendas.txt'
        if os.path.exists(local_arq):
            x = str(input('Digite "sim" para confirmar a exclusao do arquivo: ')).lower()
            if x == 'sim':
                os.remove(f'{os.path.dirname(os.path.realpath(__file__))}/vendas.txt')
                print('Arquivo excluido com sucesso')
        else:
            print(f'Arquivo não existe.')
    except FileNotFoundError:
        print('\nO arquivo não existe.')


def criar_arquivo():
    print('\n|Criar Arquivo|')
    local_arq = f'{os.path.dirname(os.path.realpath(__file__))}/vendas.txt'
    if os.path.exists(local_arq):
        print('Arquivo já existe')
    else:
        escrever_arquivo()
        print("Arquivo criado com sucesso.")


registros = {}
ler_arquivo()

while True:
    o = str(input('\nMenu:\n  0 - Finalizar o programa.\n  1 - Criar Arquivo.\n  2 - Incluir registro.'
                  '\n  3 - Excluir vendedor.\n  4 - Alterar valor de uma venda.\n  5 - Imprimir os registros.\n  '
                  '6 - Excluir o arquivo.\nEscolha uma opção: '))
    if o == '0':
        criar_arquivo()
    if o == '1':
        criar_arquivo()
        input('\nDigite qualquer coisa para voltar ao menu: ')
    if o == '2':
        incluir_registro()
        input('\nRegistro salvo com sucesso.Digite qualquer coisa para voltar ao menu: ')
    if o == '3':
        excluir_vendedor()
        input('\nDigite qualquer coisa para voltar ao menu: ')
    if o == '4':
        alterar_valor()
        input('\nDigite qualquer coisa para voltar ao menu: ')
    if o == '5':
        imprimir_registro()
        input('\nDigite qualquer coisa para voltar ao menu: ')
    if o == '6':
        excluir_arquivo()
        input('\nDigite qualquer coisa para voltar ao menu: ')
