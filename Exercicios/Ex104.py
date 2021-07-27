"""         Ex - 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a
            função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
            Ex: n = leiaInt(‘Digite um n: ‘)
"""

#   Como eu fiz.


# Função:
def leiaIntR(val):
    """
    -> Verifica se o valor é um número.
    :param val: variavel string
    :return: Se o número é inteiro ou não
    Feito por Renan Ribeiro da Silva
    """
    if val.isnumeric():
        val = int(val)
        return val
    else:
        return 0


# Programa principal:
num = str(input('Digite um valor: '))
print(f'{leiaIntR(num)} foi o valor digitado!')

# Como o Guanabara fez.


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
