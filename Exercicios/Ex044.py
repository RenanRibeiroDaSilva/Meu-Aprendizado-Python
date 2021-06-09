"""     Ex - 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
                    e condição de pagamento:
                    - À vista dinheiro/cheque: 10% de desconto
                    - À vista no cartão: 5% de desconto
                    - Em até 2x no cartão: Preço normal
                    - 3x ou mais no cartão: 20% de juros"""

# Como eu Fiz

# Variaveis:
val_produto = float(input('Qual o preço do produto: R$'))
for_pagamento = float(input("""Qual forma de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Aguardando sua opção: """))

# Resoluções matemáticas e imprimir na tela para o usuário:
if for_pagamento == 1:
    val_pro_final = val_produto - (val_produto * 0.10)
    print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
elif for_pagamento == 2:
    val_pro_final = val_produto - (val_produto * 0.05)
    print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
elif for_pagamento == 3:
    val_pro_final = val_produto
    print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
    print('Em 2 parcelas de {:.2f}'.format(val_pro_final / 2))
elif for_pagamento == 4:
    vezes = int(input('Em quantas vezes o cliente deseja parecelar? De 3x há 5x: '))
    if vezes == 3:
        val_pro_final = val_produto + (val_produto * 0.20)
        print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
        print('Em 3 parcelas de {:.2f}'.format(val_pro_final / 3))
    elif vezes == 4:
        val_pro_final = val_produto + (val_produto * 0.25)
        print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
        print('Em 4 parcelas de {:.2f}'.format(val_pro_final / 4))
    elif vezes == 5:
        val_pro_final = val_produto + (val_produto * 0.30)
        print('O produto sairá pelo preço de R${:.2f}'.format(val_pro_final))
        print('Em 5 parcelas de {:.2f}'.format(val_pro_final / 5))
    else:
        print('Opão inválida, tente novamente!')
else:
    print('Opão inválida, tente novamente!')

print('-Fim-')

#   Como o professor Guanabara fez
print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Qual o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no catão''')
opção = int(input('Qual a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sa compra será parcelada em 2x de {:.2f'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM jUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção Invalida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
