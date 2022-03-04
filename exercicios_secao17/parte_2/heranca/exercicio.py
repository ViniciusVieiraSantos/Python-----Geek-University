"""
1) Crie um novo pacote com o nome: heranca. Todas as (três) classes criadas abaixo
deverão ser salvas neste pacote.
2) Crie uma classe Equipamento com dois atributos privados.
3) Crie uma classe Computador com dois atributos sua escolha,
também privados. A classe Computador deverá herdar tudo da classe
Equipamento.
4) Crie os métodos de acesso e de modificação para todos os
atributos definidos em ambas as classes.
5) Crie uma classe TestaEquipamento, que deverá conter o método
main(), crie nela um objeto da classe Equipamento e instancie
os dois atributos que você declarou na classe Equipamento.
Crie tambpem um objeto da classe Computador, utilizando os dois
atributos declarados na rópria classe e os dois herdados da classe
Equipamento.
6) O método main() deve exibir as informações dos dois objetos criados.
7) Criar o método exibe() na classe Equipamento para mostrar os dados dessa classe
8) Reescreva o método exibe() na classe Computador, aproveitando o que já
está escrito na superclasse Equipamento
"""


class Equipamento:
    def __init__(self, nome, quantidade):
        self.__nome = nome
        self.__quantidade = quantidade


    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__nome = nova_quantidade

    def exibe(self):
        print(f'Equipamento: {self.nome} / Quantidade: {self.quantidade}')


class Computador(Equipamento):
    def __init__(self, nome, quantidade, modelo):
        super().__init__(nome, quantidade)
        self.__modelo = modelo
        self.__ligado = False

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ligado(self):
        return self.__ligado

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @ligado.setter
    def ligado(self, boleano):
        self.__nome = boleano

    def exibe(self):
        print(f'Equipamento: {self.nome} / Quantidade: {self.quantidade} / Modelo: {self.modelo} / '
              f'Ligado: {self.ligado}')


class TestaEquipamento:
    @staticmethod
    def main():
        equip_2 = Equipamento('Furadeira', 2)
        computador_2 = Computador('Computador', 1, 'MAC')
        print(f'Equipamento: {equip_2.nome} / Quantidade: {equip_2.quantidade}')
        print(f'Equipamento: {computador_2.nome} / Quantidade: {computador_2.quantidade}'
              f' / Modelo: {computador_2.modelo} / Ligado: {computador_2.ligado}')


equip_1 = Equipamento('Microondas', 3)
equip_1.exibe()
computador_1 = Computador('Computador', 1, 'Dell')
computador_1.exibe()
TestaEquipamento.main()
