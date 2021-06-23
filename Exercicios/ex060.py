"""     Ex - 060 - Faça um programa que leie um número qualquer e mostre o seu fatorial.
                    Exemplo:
                        5! = 5 x 4 x 3 x 2 x 1 = 120"""

#           Como eu fiz.

# Importat modulo matemático:
from math import factorial

# Obter dados do usuário:
num = int(input('Digite um valor: '))

# Processar dados:
fat = factorial(num)
cont = num

# Imprimir na tela para o usuário:
print('O valor fatorial de {} é {}'.format(num, fat))
print('{} != '.format(num), end='')
while cont != 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(fat)
