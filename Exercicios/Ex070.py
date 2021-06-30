"""         Ex - 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
                        o usuário vai continuar ou não. No final, mostre:
                        A) qual é o total gasto na compra.
                        B) quantos produtos custam mais de R$1000.
                        C) qual é o nome do produto mais barato.
"""

#               Como eu Fiz

# Var:
prod_mai_bart = ''
pro_mai_ba = \
    tot_gast = \
    mil_mai_cont = \
    ctd = 0

# Cabeçalho:
print(f'{"":=^60}')
print(f'{"> LISTA DE COMPRAS <":~^60}')
print(f'{"":=^60}')

# Desevenvolvimento:
while True:
    nome = str(input('Nome do produto: ')).capitalize().strip()
    prec = float(input('Valor do produto: R$'))
    ctd += 1
    tot_gast += prec

    if ctd == 1 or prec < pro_mai_ba:
        pro_mai_ba = prec
        prod_mai_bart = nome

    if prec > 1000:
        mil_mai_cont += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

    if cont == 'N':
        break
print(f'R${tot_gast:.2f} é o total a ser pago por todos os produtos!')
print(f'{mil_mai_cont} produto(s) acima de R$1000,00!')
print(f'{prod_mai_bart} foi o produto mais barato no valor de R${pro_mai_ba:.2f}')
