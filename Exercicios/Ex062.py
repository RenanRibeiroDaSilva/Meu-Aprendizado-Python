"""     Ex - 062 - Melhore o DESAFIO 61, para o usuário se ele quer mostrar mais alguns termos .
                    O programa encerrará quando ele disser que quer mostrar 0 termos."""

#               Como Eu Fiz

# Módulos:
from time import sleep

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> SUPER PROGRESSÃO ARITMÉTICA V3.0 <":=^50}')
print(f'{"":=^50}')

# Area de Desenvolvimento:

ter = int(input('Digite o primeiro termo: '))
raz = int(input('Qual a razão...........: '))
con = 0

while con != 10:
    print(ter, end='')
    print(' ->' if con < 9 else ' Pausa', end='')
    con += 1
    ter += raz
    sleep(1.2)

mai = int(input("\nDeseja ver mais quantos termos: "))
while mai != 0:
    print(ter, end='')
    print(' Pausa' if mai == 1 else ' ->', end='')
    ter += raz
    mai -= 1
    sleep(1.2)
    if mai == 0:
        mai = int(input('\nDeseja ver mais quantos termos: '))
print('Fim')


#       Como o Guanabara fez
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Priero termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
