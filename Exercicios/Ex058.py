"""         Ex - 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
                        0 e 10. Só que agora o jogador vai tertar adivinhar até acertar, mostrando no final
                        quantos palpites foram necessários para vencer."""

#           Como eu Fiz.

# Importar modulos:
from random import randint

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> JOGO DA ADVINHAÇÃO <":=^50}')
print(f'{"":=^50}')

# Imprimir na tela para o usuário:
print('Estou pensando em um número de 0 há 10, me diga.')

# Var:
palpite = 1
num_maq = randint(0, 10)
num_jog = int(input('Qual é este número: '))
# Usar while para as tentativas do usuário:
while num_maq != num_jog:
    if num_jog > num_maq:
        num_jog = int(input('Menos... Dê outro palpite: '))
        palpite += 1
    if num_jog < num_maq:
        num_jog = int(input('Mais...  Dê outro palpite: '))
        palpite += 1
print('Acertou!!! {} erá exatamente o número que eu estava pensando'.format(num_maq))
print('e você deu {} palpites até acertar a resposta correta!!!'.format(palpite))

#       Como o Guanabara Fez.
# from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
