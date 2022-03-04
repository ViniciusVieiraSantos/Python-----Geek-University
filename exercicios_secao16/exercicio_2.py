"""
2) Crie um classe Agenda que pode armazenar 10 pessoas e seja capas de
realizar as seguintes operações:
    . void armazenaPessoa(String nome, int idade, float altura);
    . void removePessoa(String nome);
    . int buscaPessoa(String nome);  // informa em que posição da agenda está a pessoa
    . void imprimeAgenda();  // imprime os dados de todas as pessoas da agenda
    . void imprimePessoa(int index);  // imprime os dados da pessoa que está na posição
                                         "i" da agenda
"""


class Agenda:
    contatos = []

    @staticmethod
    def armarzenar_contato(pessoa):
        Agenda.contatos.append(pessoa)
        input('Contato salvo com sucesso!Digite qualquer coisa para continuar: ')

    @staticmethod
    def remover_contato(nome):
        for n, pessoa in enumerate(Agenda.contatos):
            if pessoa.get_nome() == nome:
                Agenda.contatos.pop(n)
                input('Contato removido com sucesso!Digite qualquer coisa para continuar: ')
                break
        else:
            input(f'"{nome}" não foi encontrado na agenda.Digite qualquer coisa para continuar: ')

    @staticmethod
    def buscar_pessoa(nome):
        for n, pessoa in enumerate(Agenda.contatos):
            if pessoa.get_nome() == nome:
                print(f'O contato "{nome}" está salvo na posição {n+1}.')
                break
        else:
            print(f'"{nome}" não está salvo na agenda.')

    @staticmethod
    def dados_contatos():
        i = 1
        for pessoa in Agenda.contatos:
            print(f'    {i}- {pessoa.get_nome()} Idade: {pessoa.get_idade()} Altura: {pessoa.get_altura()}')
            i += 1

    @staticmethod
    def imprimir_contato(posi):

        if posi <= len(Agenda.contatos):
            print(f'Nome : {Agenda.contatos[posi - 1].get_nome()} '
                  f'Idade: {Agenda.contatos[posi - 1].get_idade()} Altura: {Agenda.contatos[posi - 1].get_altura()}\n')
        else:
            print(f'Não existe contato salvo na posição "{posi}" da agenda.')


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_altura(self):
        return self.idade


while True:
    print('\n|AGENDA|\n  0- Sair. \n  1- Salvar novo contato.\n  2- Remover contato.\n  3- Buscar contato.\n '
          ' 4- Imprimir todos contatos.\n  5- Imprimir contato.\n  0- Sair.')
    x = str(input('Digite uma opção: '))

    if x == '0':
        break

    if x == '1':
        print('\n|Salvar novo contato|')
        if len(Agenda.contatos) < 10:
            nom = str(input('Nome: '))
            ida = str(input('Idade: '))
            altu = str(input('Altura: '))
            contato = Pessoa(nom, ida, altu)
            Agenda.armarzenar_contato(contato)
        else:
            input('\nNão há espaço na agenda. Digite qualquer coisa para prosseguir.')

    if x == '2':
        print('\n|Remover contato|')
        if not Agenda.contatos:
            input('\nNão há contatos salvos na agenda. Digite qualquer coisa para prosseguir.')
        else:
            nom = str(input('Nome do contato a ser removido: '))
            Agenda.remover_contato(nom)

    if x == '3':
        if not Agenda.contatos:
            input('\nNão há contatos salvos na agenda. Digite qualquer coisa para prosseguir.')

        else:
            print('\n|Buscar contato|')
            nom = str(input('Nome: '))
            Agenda.buscar_pessoa(nom)
            input('Digite qualquer coisa para continuar: ')

    if x == '4':
        print('\n|Imprimir todos contatos|')
        if not Agenda.contatos:
            input('\nNão há contatos salvos na agenda. Digite qualquer coisa para prosseguir.')
        else:
            Agenda.dados_contatos()
            input('Digite qualquer coisa para continuar: ')

    if x == '5':
        print('\n|Imprimir contato|')
        if not Agenda.contatos:
            input('\nNão há contatos salvos na agenda. Digite qualquer coisa para prosseguir.')
        else:
            print(f'Posicões utilizadas da agenda : {len(Agenda.contatos)}')
            posicao = int(input('Imprimir contato salvo na posição: '))
            print()
            Agenda.imprimir_contato(posicao)
            input('Digite qualquer coisa para continuar: ')
