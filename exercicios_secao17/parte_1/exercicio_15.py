"""
15) Basenado-se no exercício 14 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do objeto.
"""


class Moto:

    def __init__(self, marca, modelo, cor, marcha, ligada):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor = 0
        self.maior = len(marchas) - 1
        self.ligada = ligada

    def imprimir(self):
        print(f'\nMoto:\nMarca : {self.marca}  Modelo : {self.modelo}  Cor : {self.cor} '
              f' Posição Marcha : {marchas[self.marcha]}  Ligada: {self.ligada}')

    def marcha_acima(self):
        if self.marcha >= self.maior:
            return '\nA moto ja está na ultima marcha'
        self.marcha += 1
        return f'\nA marcha atual : {marchas[self.marcha]}'

    def marcha_abaixo(self):
        if self.marcha <= self.menor:
            return '\nA moto já está no Neutro'
        self.marcha -= 1
        return f'\nA marcha atual : {marchas[self.marcha]}'


marchas = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta']
m = Moto('Bmw', 'F 750 GS', 'Azul', 3, True)
m.imprimir()
print(m.marcha_acima())
print(m.marcha_acima())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
