"""      Ex - 091 -  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
                    Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
                    sabendo que o vencedor tirou o maior número no dado."""

#               Como eu fiz.

# Módulo:
from random import randint
from time import sleep
from operator import itemgetter

# Tuplas, Listas e Dicionários:
joga = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
rank = []


print(f'{">JOGANDO OS DADOS<":=^40}')
for k, v in joga.items():
    print(f'{k} tirou {v} no dado!')
    sleep(0.75)
rank = sorted(joga.items(), key=itemgetter(1), reverse=True)
print(f'{">RANKING<":~^40}')
for i, v in enumerate(rank):
    print(f'|{i+1}º Lugar: {v[0]} tirou {v[1]} no dado!  |')
    print(f"{'|':<}{'|':->39}")
print(f'{"FIM":.^40}')

#           Como o Guanabara fez.
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
