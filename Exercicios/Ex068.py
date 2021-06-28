"""         Ex - 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
                        jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

#           Como eu fiz.

# Importar módulos:
from random import randint

# Cabeçalho:
print(f'{"":=^60}')
print(f'{"> PAR OU ÍMPAR <":~^60}')
print(f'{"":=^60}')

# Var:
cont = 0

# Desenvolvimento do programa:
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    jogador_par_impar = ' '

    while jogador_par_impar not in 'PpIi':
        jogador_par_impar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    soma = jogador + computador
    if jogador_par_impar in 'Pp':
        if soma % 2 == 0:
            cont += 1
            print(f'{jogador} + {computador} = {jogador+computador}. É par, você ganhou!')
            print(f'{"":-^60}')
        else:
            print(f'{jogador} + {computador} = {jogador+computador}. É ímpar, você perdeu!')
            print(f'{"":-^60}')
            break
    else:
        if soma % 2 == 1:
            cont += 1
            print(f'{jogador} + {computador} = {jogador+computador}. É ímpar, você ganhou!!')
            print(f'{"":-^60}')
        else:
            print(f'{jogador} + {computador} = {jogador+computador}. É par, você perdeu!')
            print(f'{"":-^60}')
            break
    print('Vamos jogar denovo...')
print(f'Parabéns, você conseguiu {cont} vitória(s)!')
print('-FIM DO JOGO! Volte sempre-')
