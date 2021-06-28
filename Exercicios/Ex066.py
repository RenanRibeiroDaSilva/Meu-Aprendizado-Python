"""     Ex - 066 - Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
                    digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
                    e qual foi a soma entre elas (desconsiderando o flag).
"""

#           Como eu fiz.

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> SOMA DE TODOS OS NÚMEROS <":~^50}')
print(f'{"":=^50}')

# Area de desenvolvimento:
laco = soma = cont = 0

while True:
    laco = int(input('Digite um número (999 para parar): '))
    print(f'{"":-^50}')
    if laco == 999:
        break
    else:
        soma += laco
        cont += 1
print(f'Você digitou {cont} números. E a soma entre eles foi {soma}!')
