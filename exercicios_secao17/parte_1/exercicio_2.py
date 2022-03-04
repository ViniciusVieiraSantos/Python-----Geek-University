"""
2) Baseando-se no exercício 1 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""


class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        print(f'Nome : {self.nome} Endereço: {self.endereco} Telefone : {self.telefone}')


pessoa = Pessoa('Joao Gomes', 'Aracruz', 344343234)
print()
pessoa.imprimir()
