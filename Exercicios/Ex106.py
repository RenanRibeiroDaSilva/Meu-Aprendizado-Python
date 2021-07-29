"""     Ex - 106 - Faça um mini-sistema que ultilize o Interactive Help do Python. O usuário vai digitar o comando
        e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
        Importante: use cores.
"""

# Como eu fiz.


# Fução:
def cab():
    print(f'\033[0;42m{"":-^40}')
    print(f'\033[0;42m{"PyHelpSystem":^40}')
    print(f'\033[0;42m{"":-^40}')


def hel(msg):
    print(f'\33[7;40m')
    help(msg)


def aces(msg):
    from time import sleep
    print(f'\033[0;43m{"":-^40}')
    print(f'\033[0;43m{"PyHelpSystem acessando: ":>20}{msg:<20}')
    print(f'\033[0;43m{"":-^40}')
    sleep(2)


# Programa principal:
while True:
    cab()
    tex = str(input('\033[mQual é a sua dúvida(FIM para finalizar): ')).strip()
    if tex.upper() == 'FIM':
        break
    else:
        aces(tex)
        hel(tex)
print('PyHelpSystem finalizado! Volte sempre...')

# Como Guanabara fez.
from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;40m'      # 6 - branco
     )


def ajuda(com):
    título(f'Acessando o manual de comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)