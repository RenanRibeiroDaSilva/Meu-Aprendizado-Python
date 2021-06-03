"""     Ex - 032 - Faça um programa que leia um ano quanquer e mostre se ele é BISSEXTO."""

#               Como eu Fiz

# Criar e receber uma varial para receber o valor do ano deseja pelo usuário
ano = int(input('Digite um ano no formato yyyy: '))

if ano % 4 != 0:
    print('O ano {} não é um ano Bissexto'.format(ano))
else:
    print('O ano {} é um ano Bissexto.'.format(ano))

#           Como o Guanabara Fez
from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))