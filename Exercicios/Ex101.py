"""     Ex - 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
        nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
        e OBRIGATÓRIO nas eleições.
"""

#           Como eu fiz.


# Definindo funções:
def voto(ano):
    """
    -> Descobre se usuário vota ou não!
    :param ano: Recebe o ano de nascimento do usuário
    :return: se o voto é OBRIGATÓRIO, OPCIONAL ou NEGADO.
    Desenvolvido por Renan Ribeiro da Silva.
    """
    from datetime import datetime
    ida = datetime.now().year - ano
    if 18 <= ida < 65:
        return f'A pessoa tem {ida} anos e o voto é OBRIGATORIO!'
    elif ida >= 65 or 16 <= ida <= 17:
        return f'A pessoa tem {ida} anos e o voto é OPCIONAL!'
    else:
        return f'A pessoa tem {ida} anos e NÃO VOTA!'


# Programa principal:
while True:
    ano_nasc = int(input('Digite o ano de nascimento: '))
    print('¨¨' * 30)
    print(voto(ano_nasc))
    print('¨¨' * 30)

    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Resposta inválida!')
    if resp in 'N':
        break
print(f'{">FIM DO PROGRAMA! Volte sempre!!!<":-^60}')

#           Como o Guanabara fez.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
