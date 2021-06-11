"""         Ex - 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

#           Como eu fiz

# Cabeçalho
print(f'{"":=^40}')
print(f'{"> Números Primos <":=^40}')
print(f'{"":=^40}')

# Variavei:
num = int(input('Digite um valor: '))
primo = 0

# Criar laço de repetição:

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[m', end='')
    print(c, end=" ")
if primo == 2:
    print('\n\033[mO número \033[33m{}\033[m é primo'.format(num))
else:
    print('\n\033[mO número {} não é primo'.format(num))
print('FIM')

#       Como o Professor Guanabara Fez
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if num % c == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c, end=''))
print('\n\033[mO número {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
