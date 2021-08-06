"""     Ex - 110 -  Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada
        resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no
        módulo criado até aqui.
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
    return res if not formato else moeda(res)


def moeda(p=0, moeda='R$'):
    """
    -> Devolve uma string formatada
    :param p: valor inserido pelo usuário
    :param moeda: tipo de moeda
    :return: valor formatado
    """
    float(p)
    return f'{moeda}{p:<4.2f}'.replace('.', ',')


def resumo(p=0, taxa_a=10, taxa_r=5):
    """
    -> Devolve de os resultados referentes ao valor formatado para o usuário
    :param p: valor definido pelo usuário
    :param taxa_a: taxa de aumento, que pode ser defenida pelo usuário
    :param taxa_r: taxa de redução, que pode ser definida pelo usuário
    :return: resultado formatado
    """
    print('-' * 30)
    print('Resumo do resultado'.center(40))
    print('-' * 30)
    print(f'Dobro do preço..: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxa_a}% de aumento.: \t{aumentar(p, taxa_a, True)}')
    print(f'{taxa_r}% de desconto..: \t{diminuir(p, taxa_r, True)}')
    print('-' * 30)
