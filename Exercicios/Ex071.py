"""         Ex - 071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
                        usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
                        cédulas de cada valor serão entregues. OBS:
                        considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

#                 Como eu fiz

# Cabeçalho:
print(f'{"":=^60}')
print(f'{"> BANCO RRS <":~^60}')
print(f'{"":=^60}')

# Var:
saque = int(input('Qual valor do saque: R$'))
tot = saque
ced = 200
con_ced = 0

# Desenvilvimento:
while True:
    if tot >= ced:
        tot -= ced
        con_ced += 1
    else:
        if con_ced > 0:
            print(f'Total de {con_ced} nota(s) de R${ced:.2f}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        con_ced = 0
        if tot == 0:
            break
print(f'{"":~^60}')
print(f'{"Volte sempre ao banco RRS!":-^60}')
print('FIM DO PROGRAMA')