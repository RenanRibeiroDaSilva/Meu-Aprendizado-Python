"""         Ex - 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
                        digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

#           Como eu Fiz

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> TABUADA <":~^50}')
print(f'{"":=^50}')

# Var:
num = 0

# Laço infinito:
while True:
    num = int(input('Digite um número (número negativo para parar): '))
    if num < 0:
        break
    print(f'{"":-^50}')
    for tabu in range(1, 11):
        print(f'{num:2} x {tabu:2} = {num * tabu:2}')
    print(f'{"":-^50}')
print(f'Fim da tabuada. Volte sempre!')

#       Como Guanabara fez

while True:
    n = int(input('Quer ver a tabuada que qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
