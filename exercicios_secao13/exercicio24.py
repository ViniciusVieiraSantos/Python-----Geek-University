"""
24) Implemente um controle simples de mercadorias em umas despensa domésticas.
Para cada produto armazene um código numérico, descrição e quantidade atual.
O programa deve ter opções para entrada e retirada de produtos, bem como
um relatório geral e um de produtos não disponíveis. Armazene os dados
em arquivo binário.
"""


def entrada_produto():
    while True:
        x = str(input('\nMenu entrada de produtos:\n- Digite "1" para cadastrar um novo produto no sistema.'
                      '\n- Digite "2" para alterar a quantidade de um produto existente.'
                      '\n- Digite "0" para sair.\nOpção: '))

        if x == '0':  # SAIR
            break

        if x == '1':  # CADASTRAR PRODUTO
            print('\nOpção 1 escolhida,cadastrar um novo produto no sistema.')
            while True:
                y = str(input('Cadastro de produto:\n-Digite "0" para sair.'
                              '\n-Digite qualquer coisa para continuar.\n '))
                if y == '0':
                    escrever_binario()
                    break
                for i in range(1, 10000):
                    if str(i) not in produtos:
                        print(f'Codigo do produto : {i}')
                        descricao = str(input('Crie uma Descrição para o produto: ')).title()
                        quantidade = int(input('Digite a quantidade atual do produto: '))
                        produtos[str(i)] = [descricao, quantidade]
                        print('Produto registrado com sucesso!')
                        break

        if x == '2':  # ALTERAR QUANTIDADE DE UM PRODUTO CADASTRADO
            alterar_produto()


def alterar_produto():
    if not produtos:
        return print("\nNão há produto cadastrado no sistema.\n")

    print('Opção 2 escolhida,alterar a quantidade de um produto existente.')
    while True:
        y = str(input('\nDigite o codigo do produto (Digite "0" para sair): '))
        if y == '0':
            escrever_binario()
            break

        elif y in produtos:
            print(f'\nProduto de codigo "{y}" encontrado:\n'
                  f'Descrição = "{produtos[y][0]}" / Quantidade = {produtos[y][1]} ')
            q = int(input(f'Digite a nova quantidade : '))
            if q < 0:
                q = 0
            produtos[y][1] = q
            print('\nQuantidade alterada com sucesso!\n')

        else:
            print(f'\nProduto de codigo "{y}"não está cadastrado no sistema!\n')


def remove_produto():
    while True:
        x = str(input('\nMenu retirada de produtos:\n- Digite "1" para remover um produto do sistema.'
                      '\n- Digite "2" para alterar a quantidade de um produto existente.'
                      '\n- Digite "0" para sair.\nOpção: '))

        if not produtos:
            return print("\nNão há produto cadastrado no sistema.\n")

        if x == '0':  # SAIR
            break

        if x == '1':  # REMOVER PRODUTO
            print('\nOpção 1 escolhida,remover um produto do sistema.')
            while True:
                y = str(input('\nDigite o codigo do produto a ser removido (Digite "0" para sair): '))
                if y == '0':
                    break

                elif y in produtos:
                    print(f'\nProduto de codigo "{y}" encontrado:\n'
                          f'Descrição = "{produtos[y][0]}" / Quantidade = {produtos[y][1]}\n')
                    q = str(input(f'\nDigite "1" para confirmar a remoçâo do produto : '))
                    if q == '1':
                        produtos.pop(y)
                        escrever_binario()
                        print('\nProduto removido com sucesso!\n')
                        relatorio()

                else:
                    print(f'\nProduto de codigo "{y}"não está cadastrado no sistema!\n')

        if x == '2':  # ALTERAR QUANTIDADE DE UM PRODUTO CADASTRADO
            alterar_produto()


def escrever_binario():
    with open("despensa.bin", "w+b") as arquivo:
        for i in produtos:
            i = str(i)
            produto = f'Codigo: {i} | Descrição: {produtos[i][0]} ' \
                      f'| Quantidade: {produtos[i][1]}\n'.encode("utf8")
            arquivo.write(produto)

    print("Informações inseridas no arquivo com sucesso!\n")


def relatorio():
    print("\n\nProdutos cadastrados no sistema:")
    if not produtos:
        return print("Não há produto cadastrado no sistema.\n")
    for i in produtos:
        i = str(i)
        print(f'Codigo: {i} | Descrição: {produtos[i][0]} | Quantidade: {produtos[i][1]}')
    str(input('Digite qualquer coisa para continua: '))
    print()


def produtos_indisponiveis():
    cont = 0
    print('\nProdutos indisponiveis:')
    if not produtos:
        return print("\nNão há produto cadastrado no sistema.\n")
    for codigo, produto in produtos.items():
        if produto[1] == 0:
            print(f'- Codigo: {codigo} | Descrição: {produto[0]} | Quantidade: {produto[1]}|')
            cont += 1

    if cont == 0:
        print('   Não há produtos indisponiveis')
    str(input('Digite qualquer coisa para continua: '))
    print()


# INICIO PROGRAMA PRINCIPAL
produtos = {}

try:
    with open('despensa.bin', 'rb') as arquivo:
        txt = arquivo.read().decode("utf8").strip().split('\n')


        """
        Ao inciar o programa,deve-se ler o arquivo binario e salvar no programa 
        para não perder informações do produtos salvas.Essas informações estão salvas no formarto:
        Codigo: 1 | Descrição: Farinha de Trigo | Quantidade: 4
        Para salvar essas informações no programa,deve-se trata-las primeiro 
        """
        substrings = ['Codigo:', 'Descrição:', 'Quantidade:']  # informações que devem ser removidas
        for linha in txt:

            for i in range(len(substrings)):
                linha = linha.replace(substrings[i], '')   # remover substrings
            linha = linha.split('|')             # criar uma lista usado | como divisor

            for j in range(len(linha)):
                linha[j] = linha[j].strip()      # tirar os espaçoes em branco
            produtos[linha[0]] = [linha[1], int(linha[2])]  # salvar o resultado


except FileNotFoundError:
    print("Arquivo 'despensa.bin' não existe.")


while True:
    x = str(input('Menu principal:\n- Digite "1" para entrada de produto no sistema.'
                  '\n- Digite "2" para remover um produto do sistema.'
                  '\n- Digite "3" para gerar um relatorio.'
                  '\n- Digite "4" mostrar produtos não disponiveis.'
                  '\n- Digite "0" para sair.\nOpção: '))
    if x == '0':
        break
    elif x == '1':
        entrada_produto()

    elif x == '2':
        remove_produto()

    elif x == '3':
        relatorio()
    elif x == '4':
        produtos_indisponiveis()
