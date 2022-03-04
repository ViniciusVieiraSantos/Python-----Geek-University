"""
10) Baseando-se no exercício 9 adicione um método construtor que permita
a definição de todos os atributos no momento da instânciação do objeto
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
