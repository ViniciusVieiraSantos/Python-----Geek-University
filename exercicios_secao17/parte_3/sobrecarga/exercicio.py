"""
1) Crie um novo pacote chamado sobrecarga.
2) Crie uma classe Pessoa.
3) Na classe Pessoa crie 3 variáveis de instância: código, nome, idade
4) Crie um método exibe(), que exiba o conteúdo de todas as variáveis
declaradas na classe em questão
5) Crie uma sobrecarga no método exibe() que receba como parâmetro um
número inteiro e decida por meio do valor desse parâmetro se a idade será
exibida ou não. Para isso use o seguinte critério: se o valor do parâmetro
for igual a 1, imprima idade, se não, não imprima a idade, mas apenas as
outras variáves de instância.
6) Crie um construtor padrão explícito para a classe Pessoa, esse construtor
deverá exibir uma mensagem: "Construtor padrão"
7) Crie uma classe chamada TestaPessoa que instancie um objeto da classe
Pessoa usando o construtor padrão
8) Ainda na classe TestaPessoa, inicialize as variáveis de instância:
código, nome e idade com valores à sua escolha e acione o método exibe(),
sem nenhum parâmetro
9) Repita a operação da questão anterior, acionando o método exibe(),
passando a ele um argumento inteiro de valor 1
10) Repita o que foi feito na questão anterior, só que desta vez, passando
um argumento diferente de 1
11) Crie um construtor sobrecarregado que permita instanciar objetos com
os 3 valores sendo inicializados por valores passados como parâmetros
12) Na classe TestaPessoa instancie um objeto usando o segundo construtor (com
os 3 parâmetros).
13) Exiba os dados do objeto que foi instanciado na questão anteiror por
meio do método exibe() sem argumentos
"""


class Pessoa:
    def __init__(self, codigo, nome, idade):
        print("\nConstrutor padrão")
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def exibe(self, numero=0):

        print(f'\nCodigo: {self.codigo} | Nome: {self.nome}{f" | Idade: {self.idade}" if numero == 1 else ""}')


class TestaPessoa:
    pessoa = Pessoa(4, 'alex', 4)
    pessoa.exibe()
    pessoa.exibe(1)
    pessoa.exibe(2)

    def __init__(self, idade=0, nome='não informado', codigo=0):
        self.nome = nome
        self.idade = idade
        self.codigo = codigo

    @classmethod
    def instanciar(cls):
        pessoa = cls(3, 'vitor', 13)
        return pessoa

    def exibe(self, numero=0):

        print(f'\nCodigo: {self.codigo} | Nome: {self.nome}{f" | Idade: {self.idade}" if numero == 1 else ""}')


pessoa_1 = TestaPessoa()
pessoa_2 = TestaPessoa()
pessoa_2.exibe()
pessoa_1.instanciar().exibe()
