"""        Ex - 098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
            início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
            a) de 1 até 10, de 1 em 1
            b) de 10 até 0, de 2 em 2
            c) uma contagem personalizada
"""

#       Como eu fiz.

# Módulo:
from time import sleep


# Função:
def contador(a, b, c):
    print('=-' * 30)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contando de {a} até {b} de {c} em {c}:')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= c
        print('FIM!')


# Programa pricipal:
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 30)
inicio = int(input('Digite o número incial: '))
final = int(input('Digite o núemro final: '))
passo = int(input('Digite o passo da contagem: '))
contador(inicio, final, passo)