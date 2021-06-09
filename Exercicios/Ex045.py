"""     Ex - 45 - Crie um programa que faça o computador jogar Jokenpô com você."""

# Como eu fiz
"""
# Importar modulo random:
from random import randint
from time import sleep

print(f'{" JOKENPÔ ":=^40}')
print('''Vamos jogar? 
[ 1 ] SIM
[ 0 ] NÃO''')
inic = int(input('Estou te aguardando...'))

if inic == 1:

    print('''Esolha entre: 
    PAPEL
    PEDRA
    TESOURA''')
    usuario = str(input('Qual sua escolha..:')).upper()

    # Criar Var:
    num = randint(1, 3)

    # Criar condicional
    if num == 1:
        print('Você escolheu {}.'.format(usuario))
        print('Eu escolho PAPEL.')
    elif num == 2:
        print('Você escolheu {}.'.format(usuario))
        print('Eu escolho PEDRA.')
    else:
        print('Você escolheu {}.'.format(usuario))
        print('Eu escolho TESOURA.')
else:
    print('Que pena!')

print('''Se você jogou PEDRA eu VENCI!!!
Se você jogou TESOURA você VENCEU!!!
Se você também jogou PAPEL nós empatamos!!!''')
print('-FIM-')
"""
#       Como o Guanabara fez
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOUZA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATER')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCER')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCER')
    elif jogador == 1:
        print('EMPATER')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCER')
    elif jogador == 2:
        print('EMPATER')
    else:
        print('JOGADA INVÁLIDA!')