"""         Ex - 038 - Escreva um programa que leia dois números inteiros e compare-os , mostrando na tela
                        uma mensagem:
                        - O primeiro valor é maior
                        - O segundo valor é maior
                        - Não existe valor maior, os dois são iguais """

#               Como eu fiz

# Criar uma variável para receber o valor dado pelo usuário
num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite mais um número: '))

# Criar uma variável para reconhecer qual é o maior valor

if num_1 > num_2:
    print('O primeiro valor é maior!')
elif num_2 > num_1:
    print('O segundo valor é maior!')
elif num_1 == num_2:
    print('Não existe valor maior, os dois são iguais!')
print('-Fim-')

#       Como o Prefessor Guanabara Fez
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO número é maior')
elif n2 > n1:
    print('O SEGUNDO número é maior')
else:
    print('Os dois valores são IGUAIS')

