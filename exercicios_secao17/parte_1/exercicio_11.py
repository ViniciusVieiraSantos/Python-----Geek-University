"""
11) Baseando-se no exercício 10 adicione os métodos marchaAcima e
marchaAbaixo que deverão efetuar a troca de marchas, onde o método
marchaAcima deverá subir uma marcha, ou seja, se a moto estiver em
primeira marcha, deverá ser trocada para segunda marcha e assim por diante.
O método marchaAbaixo deverá realiar o oposto, ou seja, descer a marcha.
O método imprimir deve ser modificado de forma a mostrar na tela os valores
de todos os atributos.
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

    def marcha_acima(self):
        if self.marcha >= 4:
            return '\nA moto ja está na ultima marcha'
        self.marcha += 1
        return f'\nA marcha atual : {marchas[self.marcha]}'

    def marcha_abaixo(self):
        if self.marcha <= 0:
            return '\nA moto já está no Neutro'
        self.marcha -= 1
        return f'\nA marcha atual : {marchas[self.marcha]}'


marchas = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta']
m = Moto('Bmw', 'F 750 GS', 'Azul', 3)
m.imprimir()
print(m.marcha_acima())
print(m.marcha_acima())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())


