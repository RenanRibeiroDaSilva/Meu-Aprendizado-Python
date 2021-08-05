"""     Ex - 109 - Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
     desafio 108.
"""


def aumentar(p=0, tax=0, formato=False):
    """
    -> Aumenta o valor inicial em uma porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :param formato: formatação do valor
    :return: valor inicial somada a taxa
    """
    res = p + (p * tax/100)
    return res if not formato else moeda(res)


def diminuir(p=0, tax=0, formato=False):
    """
    -> Diminui o valor inicial em um porcentagem definida pelo usuário
    :param p: valor inicial
    :param tax: valor da taxa
    :param formato: formatação do valor
    :return: valor inicial subtraído a taxa
    """
    res = p - (p * tax/100)
    return res if not formato else moeda(res)


def dobro(p=0, formato=False):
    """
    -> Dobra o valor inicial
    :param p: valor inicial
    :param formato: formatação do valor
    :return: valor inicial em dobro
    """
    res = p * 2
    return res if not formato else moeda(res)


def metade(p=0, formato=False):
    """
    -> Divide o valor inicial
    :param p: valor inicial
    :param formato: formatação do valor
    :return: valor dividido pela metade
    """
    res = p / 2
    return res if formato is True else moeda(res)


def moeda(p=0, moeda='R$'):
    """
    -> Devolve uma string formatada
    :param p: valor inserido pelo usuário
    :param moeda: tipo de moeda
    :return: valor formatado
    """
    float(p)
    return f'{moeda}{p:<4.2f}'.replace('.', ',')
