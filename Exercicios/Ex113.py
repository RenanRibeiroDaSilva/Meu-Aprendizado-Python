"""     Ex - 113 - eescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma
funcionalidade."""


def read_int(msg):
    """
    -> Válida um número inteiro.
    :param msg: valor digitado pelo usuário.
    :return: valor inteiro validado
    """
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não informar os dados!\033[m')
            break
        else:
            return i


def read_float(msg):
    """
    -> Válida um número Real
    :param msg: valor digitado pelo usuário
    :return: valor float validado
    """
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não informar os dados!\033[m')
            break
        else:
            return r


n1 = read_int('Digite um número inteiro: ')
n2 = read_float('Digite um número Real: ')
print(f'Os números digitados foram {n1} e {n2}!')
