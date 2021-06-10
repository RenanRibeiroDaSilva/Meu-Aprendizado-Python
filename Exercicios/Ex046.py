"""     Ex - 046 - Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artificio, indo
                    de 10 até 0. com uma pausa de 1 segundo."""

#           Como eu Fiz

# Importar modulos necessarios:
from time import sleep
import emoji

print(f'{"Contagem Regrassiva":=^40}')

# Iniciar o programa:
print('''Deseja iniciar a contagem?
[ 1 ] SIM
[ 0 ] NÃO''')
inic = int(input('Aguardando... '))

if inic == 1:
    print('Iniciando Contagem REGRESSIVA...')
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print(emoji.emojize(":collision:"), u"\U0001F4A5", u"\U0001F4A5", u"\U0001F4A5", u"\U0001F4A5")
    print(u"\U0001F4A5", u"\U0001F4A5", u"\U0001F4A5", u"\U0001F4A5", u"\U0001F4A5")
elif inic != 0 and inic != 1:
    print('Opção invalida!')
else:
    print('Desligando...')
    sleep(3)
print('-Fim-')

#           Como o Professor Guanabara fez
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')