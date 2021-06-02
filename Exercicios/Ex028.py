"""     Ex - 028 - Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
                    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

                    O  programa deverá escrever na tela se o usuário venceu ou perdeu."""

#                       COMO EU FIZ!

# importar a biblioteca random e usar o metodo randint(a,b)
import random

# Variavel com o valor que o computador irá encontrar randomincamente entre 0 e 5
num_pensado = random.randint(0, 5)

# Pedir e criar uma variavel com o número proposto pelo usuário.
num_resposta = int(input('Entre 0 e 5, em qual número eu estou pensando? '))

# Mostrar para o usuário se ele acertou ou não o resultado.
if num_resposta == num_pensado:
    print('PARABÉNS!  Você acertou.')
else:
    print('NÃO FOI DESSA VEZ! Eu estava pesando no número {}.'.format(num_pensado))
print('-->FIM<--')


#                    COMO O PROFESSOR GUANABARA FEZ
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR".
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3) # Faz o programa esperar pelo tempo que foi determinado em segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}.'.format(computador, jogador))


