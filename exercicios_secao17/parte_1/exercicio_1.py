"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome,
endereço e telefone e, o método imprimir. O método imprimir deve mostra todos
os valores de todos os atributos.
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
