def verificar_nome(nome):
    """Função que recebe um nome e verifica se o mesmo é válido ou não.
    Caso o nome seja válido retorna True, caso contrário retorna False"""

    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]

    try:

        for caractere in nome:

            if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
                return False

        return True

    except AttributeError:
        return False

    except ValueError:
        return False

    except TypeError:
        return False


def verificar_telefone(telefone):
    """Função que recebe um nome e verifica se o mesmo é válido ou não.
    Caso o nome seja válido retorna True, caso contrário retorna False"""

    caracteres_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ",
                          "+", "(", ")", "-"]

    try:

        valido = False

        for caractere in str(telefone):

            if str(caractere) in caracteres_validos:
                valido = True

            else:
                valido = False
                break

        return valido

    except AttributeError:
        return False

    except ValueError:
        return False
