"""         Ex - 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
                        O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
                         ele vai pagar.

                         Calcule o valor da presatação mensal, sabendo que ela não pode exceder 30% do salário
                         ou então o empréstimo será negado."""

#                       Como eu Fiz

from time import sleep
print('\033[m-=\033[m' * 30)
print('|                  \033[4;33mEmprestimo imobiliário\033[m                  |')
print('\033[m-=\033[m' * 30)

''' Criar variavel '''

val_casa = float(input('Qual o valor da casa?.................................. R$'))
sala_usua = float(input('Qual o salario do usuário?............................. R$'))
ano_pag = float(input('Em quantos anos o usuário pretente pagar o emprestimo? '))
print('Calculando...')
sleep(3)
# print('{} {} {}'.format(casa, sala, ano_pag))

''' Calculos matemáticos '''

# Quantidade de prestações
qua_prestacao = ano_pag * 12
# Valor das prestações
val_prestacao = val_casa / qua_prestacao
# Verificação do emprestimo
ver_emprestim = sala_usua * 0.30

''' Criar uma condição para verificar se o emprestimo será liberado'''

if val_prestacao > ver_emprestim:
    print('\033[31mEMPRESTIMO NEGADO!\033[m')
    print('As parcelas ficaram no valor de R${:.2f}'.format(val_prestacao))
    print('Um valor maior que 30% do salário do usuário')
else:
    print('\033[32mEMPRESTIMO CONCEDIDO!\033[m')
    print('As parcelas ficaram no valor de R${:.2f}'.format(val_prestacao))
    print('E está dentro das regras para conceder o emprestimo')


#          Como o Guanabara Fez

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quanto anos de finaciamento?'))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {}anos'.format(casa, anos), end = '')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
