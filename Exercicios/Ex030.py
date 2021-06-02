"""     Ex - 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR."""

#               Como eu Fiz

# Criar uma variavel para receber um valor do usuário
num = int(input('Digite um valor: '))
impar = num % 2

if impar == 1:
    print('O número {} é IMPAR'.format(num))
else:
    print('O número {} é PAR'.format(num))
print('--Fim--')

#       Como o professor Guanabara Fez
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))
