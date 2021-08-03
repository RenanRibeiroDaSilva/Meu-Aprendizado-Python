"""     Ex - 107 -  Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
        dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


# Aumenta o valor inicial em uma porcentagem definida pelo usuário:
def aumentar(p, tax):
    """
    -> Aumenta o valor inicial em uma porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :return: valor inicial somada a taxa
    """
    res = p + (p * tax/100)
    return res


def diminuir(p, tax):
    """
    -> Diminui o valor inicial em um porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :return: valor inicial subtraído a taxa
    """
    res = p - (p * tax/100)
    return res


def dobro(p):
    """
    -> Dobra o valor inicial
    :param p: valor inicial
    :return: valor inicial em dobro
    """
    res = p * 2
    return res


def metade(p):
    """
    -> Divide o valor inicial
    :param p: valor inicial
    :return: valor dividido pela metade
    """
    res = p / 2
    return res
