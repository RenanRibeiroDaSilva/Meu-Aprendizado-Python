"""         Ex - 088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
                        quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
                        tudo em uma lista composta.
"""
#           Como eu fiz

# Módulos:
from random import randint
from time import sleep

# Lista:
palpi = []

# var:
qtd = int(input('Quantos palpites você deseja: '))

# Laço:
for c in range(0, qtd):
    jogo = [randint(1, 60), randint(1, 60), randint(1, 60),
            randint(1, 60), randint(1, 60), randint(1, 60)]
    for n in range(0, 6):
        if jogo[n] == jogo[n-1]:
            randint(1, 60)
    jogo.sort()
    palpi.append(jogo[:])
    jogo.clear()

# Resultado:
for c in range(0, qtd):
    print(f'Jogo{c + 1:2}:', end='')
    for n in range(0, 6):
        print(f'[{palpi[c][n]:2}]', end='')
        sleep(0.5)
    print()
    sleep(0.5)
print('Fim dos palpites. Volte sempre!')

#           Como o Guanabara fez.
lista = list()
jogos = list()
print('-' * 30)
print('       JOGO NA MEGA SENA        ')
print('-' * 30)
quant = int(input('Quantos jogso você quer que eu sortei? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '<BOA SORTE!', '-=' * 5)
