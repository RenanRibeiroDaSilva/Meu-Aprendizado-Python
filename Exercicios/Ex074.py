"""             Ex - 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
                            disso, mostre a listagem de números gerados e também indique o menor e o maior valor
                            que estão na tupla.
"""

#           Como eu fiz.

# Módulo:
from random import randint
cont = 0

# Tupla:
lista = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print('O valores sorteados foram: ', end='')
for i in lista:
    cont += 1
    print(i, end='')
    print(' ' if cont < 5 else '\n', end='')

cont = maior = 0
for c in lista:
    cont += 1
    if cont == 1 or c > maior:
        maior = c

cont = menor = 0
for c in lista:
    cont += 1
    if cont == 1 or c < menor:
        menor = c
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')

#           Como o Guanabara fez
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')