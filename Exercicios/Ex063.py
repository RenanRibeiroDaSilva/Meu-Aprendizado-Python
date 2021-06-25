"""             Ex - 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
                            elementos de um Sequência de Fibonacci.
                            Exemplo:
                            0 - 1 - 1 - 2 - 3 - 5 - 8..."""

#           Como eu fiz

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> SEQUÊNCIA DE FIBONACCI <":=^50}')
print(f'{"":=^50}')

# Receber dados do usuario:
ele = int(input('Quanto elementos gostaria de visualizar: '))
fn = 0
fn1 = 0
fn2 = 1
cou = 0

while cou < ele:
    print('{}'.format(fn), end='')
    print(' - ' if cou < ele - 1 else ' Acabou...\n', end='')
    fn1 = fn2
    fn2 = fn
    fn = fn1 + fn2
    cou += 1
print(f'{"":-^50}')
print('Fim')

#               Como o Guanabara fez
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
print('-'*30)