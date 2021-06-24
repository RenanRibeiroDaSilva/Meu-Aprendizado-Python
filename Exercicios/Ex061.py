""" Ex - 61 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
                mostrando os 10 primeiros termos da progressão usando a estrutura while."""

#   Como eu Fiz

# Modulos:
from time import sleep

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> TERMOS DE UMA PA 2.0 <":=^50}')
print(f'{"":=^50}')

# Area de desenvolvimento:
pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão.........: '))
cou = 0

while cou != 10:
    print(pri, end='')
    print(' ->' if cou < 9 else ' ->FIM', end='')
    cou += 1
    pri += raz
    sleep(1)

#       Como o professor Guanabara fez
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')