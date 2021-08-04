"""     Ex - 108 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
        números como um valor monetário formatado.
"""


def aumentar(p=0, tax=0):
    """
    -> Aumenta o valor inicial em uma porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :return: valor inicial somada a taxa
    """
    res = p + (p * tax/100)
    return res


def diminuir(p=0, tax=0):
    """
    -> Diminui o valor inicial em um porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :return: valor inicial subtraído a taxa
    """
    res = p - (p * tax/100)
    return res


def dobro(p=0):
    """
    -> Dobra o valor inicial
    :param p: valor inicial
    :return: valor inicial em dobro
    """
    res = p * 2
    return res


def metade(p=0):
    """
    -> Divide o valor inicial
    :param p: valor inicial
    :return: valor dividido pela metade
    """
    res = p / 2
    return res


def moeda(p=0, moeda='R$'):
    """
    -> Devolve uma string formatada
    :param p: valor inserido pelo usuário
    :param moeda: tipo de moeda
    :return: valor formatado
    """
    return f'{moeda}{p:<4.2f}'.replace('.', ',')