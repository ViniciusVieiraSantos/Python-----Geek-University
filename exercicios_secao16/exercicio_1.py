"""
1) Crie uma classe para representar uma pessoa, como os atirbutos privados de
nome, idade e altura. Crie os métodos públicos necessários para sets e gets e
também um método para imprimir os dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir_dados(self):
        print(f'Nome: {self.__nome} Idade: {self.__idade} Altura: {self.__altura}')

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura


pessoa1 = Pessoa('Vinicius', '15', '1.6')
pessoa2 = Pessoa('Vagner', '35', '1.6')

print(Pessoa.get_nome(pessoa2))
