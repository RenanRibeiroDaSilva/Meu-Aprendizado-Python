"""         Ex - 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
                        mostre a média entre todos os valores lidos e qual foi o maior e o menor valores lidos.
                        O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

#           Como eu fiz.

# Módulos:
from time import sleep

# Cabeçalho:
print(f'{"":~^50}')
print(f'{"> MÉDIA DE TODOS OS NÚMEROS <":-^50}')
print(f'{"":~^50}')

# Var:
num = med = mai = men = som = con = 0
inc = 'S'

# Programa:
while inc == 'S':
    num = int(input('Digite um valor: '))
    som += num
    con += 1

    if con == 1:
        mai = men = num
    else:
        if num < men:
            men = num
        if num > mai:
            mai = num

    sleep(0.2)
    inc = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if inc != 'S' and inc != 'N':
        sleep(0.2)
        inc = str(input('Opção inválida! Por favor selecione entre [S/N]: ')).upper().strip()[0]

med = som / con

print(f'{"":-^50}')
print('Você digitou {} números e a média entre ele foi de {}'.format(con, med))
print('O maior valor digitado foi {} e o menor foi {}.'.format(mai, men))

#       Como o Guanabara fez.
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
