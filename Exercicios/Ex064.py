"""         Ex - 064 - Crie um programa que leia vários números inteiros pelo teclado.
                        O programam só vai parar quando o usuário digitar o valor 999,
                        que é a condição de parada. No final, mostre quantos números
                        foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

#           Como eu fiz.
from time import sleep

# Cabeçalho:
print(f'{"":~^50}')
print(f'{"> SOMA DE TODOS OS NÚMEROS <":-^50}')
print(f'{"":~^50}')

# Desenvolvimento do programa:
print('Caso queira parar digite [999]')
num = int(input('Digite um número: '))
som = 0
cot = 0
while num != 999:
    cot += 1
    som = som + num
    num = int(input('Digite novamente um valor: '))
    sleep(0.25)
print(f'{"":~^50}')
print('Você digitou um total de {} vezes e a soma entre eles é de {}'.format(cot, som))

#           Como o Guanbara fez

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitouu {} números e a soma entre eles foi {}'.format(cont, soma))
