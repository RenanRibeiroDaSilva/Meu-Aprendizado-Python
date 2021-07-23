"""         Ex - 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
            indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
             mostrado ou não na tela o processo de cálculo do fatorial.
"""

#       Como eu fiz.


# Definindo função:
def fatorial(num, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param num: O número a ser calculado.
        :param show: (opcional) Mostra ou não a conta.
        :return: O valor do Fatorial de um número n.
        """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal:
while True:
    print(f'{"":-^50}')
    nu = int(input('Digite um valor: '))
    while True:
        mo = str(input('Deseja mostrar o processo de calculo [S/N]: ')).strip().upper()[0]
        print(f'{"":¨^50}')
        if mo in 'SN':
            break
        print('ERRO! Resposta inválida!')
    if mo == 'S':
        mos = True
    else:
        mos = False
    print(f'O fatorial de {nu} é:')
    print(f'{fatorial(nu, mos)}')
    print(f'{"":¨^50}')
    while True:
        res = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

        if res in 'SN':
            break
        print('ERRO! Resposta inválida!')
    if res == 'N':
        break
print(f'{"FINALIZANDO O PROGRAMA!":~^50}')


#           Como o Guanabara fez.
def factorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal:
print(factorial(5, show=True))
help(factorial)
