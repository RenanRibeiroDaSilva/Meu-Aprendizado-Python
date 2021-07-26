"""         Ex - 103 -  Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
            o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
             mesmo que algum dado não tenha sido informado corretamente.
"""

# Como eu fiz.


# Função:
def fichaR(nome='<desconhecido>', gols=0):
    """
    -> Imprime o nome do jogador e quantos gols foram feitos
    :param nome: Nome do jogador
    :param gols: Quantidade de gols
    :return: Nada
    Feito por Renan Ribeiro
    """
    if gols > 1 or gols == 0:
        print(f'O jogador {nome} fez {gols} gols!')
    else:
        print(f'O jogador {nome} fez {gols} gol!')


# Programa principal:
n = str(input('Nome: ')).strip().title()
g = str(input('Quantos gols: ')).strip()
print(f'{"":-^50}')
if g.isnumeric():  # isnumeric sendo usado para verificar se uma string pode ser um número
    g = int(g)
else:
    g = 0
if n == '':
    fichaR(gols=g)
else:
    fichaR(n, g)
print(f'{"":-^50}')

# Como o Guanabara Fez.


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')


# Programa principal:
n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
