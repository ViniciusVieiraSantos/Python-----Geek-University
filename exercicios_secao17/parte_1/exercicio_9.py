"""
9) Escreva um código que apresente a classe Moto, com
atributos marca, modelo, cor e marcha e, o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O
atributos marcha indica em que a marcha a Moto se encontra no momento, sendo
representado de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.
"""


class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha

    def imprimir(self):
        print(f'\nMoto:\nMarca : {self.marca}  Modelo : {self.modelo}  Cor : {self.cor} '
              f' Posição Marcha : {marchas[self.marcha]}')


marchas = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta']
m = Moto('Bmw', 'F 750 GS', 'Azul', 3)
m.imprimir()
