"""
12) Basenado-se no exercicio 11 adicione os atributos menorMarcha
e maiorMarcha, onde o atributo menorMarcha indica qual será a menor
marcha possível para a moto e o atributo maiorMarcha indica qual será
a maior marcha possível. Desta forma os métodos marchaAcima e marchaAbaixo
deve ser reescritos de forma a não permitirem a troca de marchar para valores
abaixo da menorMarcha e acima da maiorMarcha. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.
"""


class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor = 0
        self.maior = len(marchas) - 1

    def imprimir(self):
        print(f'\nMoto:\nMarca : {self.marca}  Modelo : {self.modelo}  Cor : {self.cor} '
              f' Posição Marcha : {marchas[self.marcha]}')

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
m = Moto('Bmw', 'F 750 GS', 'Azul', 3)
m.imprimir()
print(m.marcha_acima())
print(m.marcha_acima())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
print(m.marcha_abaixo())
