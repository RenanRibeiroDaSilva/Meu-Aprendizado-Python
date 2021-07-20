"""         Ex - 099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
            inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


#               Como eu fiz.
from time import sleep


# Definindo funções:
def maiorR(num):
    for i, n in enumerate(num):
        if i == 0 or n > mai:
            mai = n
    print(mai)


# Programa pricipal:
nume = []

while True:
    num = int(input('Digite um valor: '))
    nume.append(num)
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Resposta invalida!')
    if resp == 'N':
        break

print(f'Os valores digitados foram {nume}')
print(f'E o maior valor digitado foi ', end='')
maiorR(nume)
print('FIM')

#           Como o Guanabara fez.


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}')


# Programa pricipal:
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()