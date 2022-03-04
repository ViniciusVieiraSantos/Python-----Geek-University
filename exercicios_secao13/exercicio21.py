"""
21) Crie um programa que receba como entrada o número de alunos de uma
disciplina. Aloque dinamicamente em uma estrutura para armazenar as informações
a respeito desses alunos: nome do aluno e sua nota final. Use nomes com no máximo
40 caracteres. Em seguida, salve os dados dos alunos em um arquivo binário.
Por fim, leia o arquivo e mostre o nome do aluno com a maior nota.
"""
from exercicios_secao13.verifica_nome_telefone import verificar_nome

try:
    qtd_alunos = int(input("Digite a quantidade de alunos: "))
    nome_alunos = []
    nota_alunos = []
    for aluno in range(qtd_alunos):
        while True:
            nome = str(input(f"\nDigite o nome do aluno {aluno+1}: ")).strip().title()

            if verificar_nome(nome):
                # Caso nome fornecido tenha 40 caracteres ou mais, irá pegar apenas os primeiros
                # 40 caracteres do nome, caso o nome não contenha 40 caracteres ele irá preencher até
                # 40 caracteres usando espaços em branco
                novo_nome = nome[0:40:1] if len(nome) >= 40 else nome + " " * (40 - len(nome))
                nota = float(input(f"Digite a nota final do {nome}: "))
                nome_alunos.append(novo_nome)
                nota_alunos.append(nota)
                break

            else:
                print("\nNome inválido!")

    with open("alunos_notas.bin", "ab") as arquivo:

        for i in range(qtd_alunos):
            linha = f"{nome_alunos[i]} {nota_alunos[i]}\n".encode("utf8")

            arquivo.write(linha)

    print("\nInformações inseridas no arquivo com sucesso!")

    with open("alunos_notas.bin", "rb") as ler_arquivo:

        linhas = ler_arquivo.read().decode("utf8").splitlines()

        aluno = max(linhas, key=lambda dado: float(dado[41::]))

        print(f"\nO aluno com a maior nota é o {aluno[0:40:1]}")


except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
except ValueError:
    print("\nO valor fornecido é inválido!")
