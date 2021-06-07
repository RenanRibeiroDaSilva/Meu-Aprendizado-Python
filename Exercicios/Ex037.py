"""         Ex - 037 - Escreva um progama que leia um número inteiro qualquer e peça para o usuário
                        escolher qual será a base de conversão

                        -1 para binário
                        -2 para octal
                        -3 para hexadecimal"""

#               Como eu fiz

# Criar a variavel e receber os dados do usuário.

num = int(input('Digite o valor que deseja converter: '))

# Criar o menu de seleção para o usuário escolher em que base será convertida.
print('Digite [1] para binário')
print('Digite [2] para octal')
print('Digite [3] para hexadecimal')
conv = int(input('Escolha para qual base númerica você deseja converter: '))

# Criar a condição para efetuar os calculos.
if conv == 1:
    print('O valor {} em Binário = {}'.format(num, bin(num)))
elif conv == 2:
    print('O valor {} em Octal = {}'.format(num, oct(num)))
else:
    print('O valor {} em Hexadecimal = {}'.format(num, hex(num)))

# Finalizar o programa
print('-Fim-')

#               Como o professor Guanabara fez
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para converção: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção =  int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
