"""
16) Basenado-se no exercício 15 adicione os métodos ligar e deligar que
deverão mudar o conteúdo do atibuto ligada conforme o caso.
"""


class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor = 0
        self.maior = len(marchas) - 1
        self.ligada = False

    def imprimir(self):
        print(f'\nMoto:\nMarca : {self.marca}  Modelo : {self.modelo}  Cor : {self.cor} '
              f' Posição Marcha : {marchas[self.marcha]}  Ligada: {self.ligada}')

    def marcha_acima(self):
        if self.marcha >= self.maior:
            return '\nA moto ja está na ultima marcha.'
        self.marcha += 1
        return f'\nA marcha atual : {marchas[self.marcha]}'

    def marcha_abaixo(self):
        if self.marcha <= self.menor:
            return '\nA moto já está no Neutro.'
        self.marcha -= 1
        return f'\nA marcha atual : {marchas[self.marcha]}'

    def ligar(self):
        if self.ligada:
            return '\nA moto já esta ligada.'
        self.ligada = True
        return '\nA moto foi ligada.'

    def desligar(self):
        if not self.ligada:
            return '\nA moto já esta desligada.'
        self.ligada = False
        return '\nA moto foi desligada.'


marchas = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta']
m = Moto('Bmw', 'F 750 GS', 'Azul', 3)
m.imprimir()
print(m.ligar())
print(m.ligar())
print(m.desligar())
print(m.desligar())
print(m.marcha_acima())
print(m.marcha_acima())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
