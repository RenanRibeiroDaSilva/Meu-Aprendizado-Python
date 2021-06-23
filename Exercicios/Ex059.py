"""         Ex - 059 - Crie um programa que leia dois valores e mostre um menu como mostra o exemplo abaixo:
                        Seu programa deverá realizar a operação solicitada em cada caso.
                        [1] Somar.
                        [2] Multipicar.
                        [3] Maior
                        [4] Novos números
                        [5] Sair do programa"""

#           Como eu fiz

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> MENU <":=^50}')
print(f'{"":=^50}')

# Receber informações do usuario:
num_1 = float(input('Digite um valor.....: '))
num_2 = float(input('Digite mais um valor: '))
menu = 0
# Criando um menu para o usuario:
while menu != 5:
    print(f'{"":-^50}')
    print(f'{"| Escolha uma das opções abaixo! |":^50}')
    print(f'{"| [ 1 ] SOMA                     |":^50}')
    print(f'{"| [ 2 ] MULTIPICAÇÃO             |":^50}')
    print(f'{"| [ 3 ] MAIOR VALOR              |":^50}')
    print(f'{"| [ 4 ] NOVOS VALORES            |":^50}')
    print(f'{"| [ 5 ] SAIR DO PROGRAMA         |":^50}')
    menu = int(input('          Qual opção...: '))
    if menu == 1:
        print('A Soma entre {} e {} é igual há {}'.format(num_1, num_2, num_1 + num_2))
    elif menu == 2:
        print('{} multiplicado por {} é igual há {}'.format(num_1, num_2, num_1 * num_2))
    elif menu == 3:
        if num_1 > num_2:
            print('{} é maior do que {} !'.format(num_1, num_2))
        else:
            print('{} é maior do que {} !'.format(num_2, num_1))
    elif menu == 4:
        print('Informe novos valores: ')
        num_1 = float(input('Digite um valor.....: '))
        num_2 = float(input('Digite mais um valor: '))
    elif menu == 5:
        print('Finalizando programa...')
    else:
        print('Opção Inválida tente novamente: ')
    print(f'{"":-^50}')
print('Fim')

#       Como o professor Guanabara Fez
"""
from time import sleep
n1 = int(input('Primeiro valor: ))
n2 = int(input('Segundo valor: ))
opção = 0 
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!) 
"""
