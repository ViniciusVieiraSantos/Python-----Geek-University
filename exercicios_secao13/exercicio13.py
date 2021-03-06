"""
13) Faça um programa que permita que o usuário entre com diversos nomes e telefone
para cadastro, e crie um arquivo com essas informações, uma por linha. O usuário
finaliza a entrada com '0' para o telefone.
"""
from exercicios_secao13.verifica_nome_telefone import verificar_nome, verificar_telefone


try:

    while True:

        nome = str(input("Digite um nome: ")).strip().title()

        if verificar_nome(nome) and len(nome) > 0:

            telefone = str(input("Digite um número de telefone,digite '0' para finalizar: ")).strip()
            print()

            if verificar_telefone(telefone):

                with open("lista_telefone.txt", "a", encoding="utf-8") as arquivo:

                    if telefone != '0':
                        informacoes = nome + ";" + telefone
                        arquivo.write(informacoes+"\n")

                    else:
                        break

            else:
                print("Telefone inválido!\n")

        else:
            print("\nNome inválido!\n")

    print("Informações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")


