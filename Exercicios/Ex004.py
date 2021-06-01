'''Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as imformações possíveis sobre ele'''

palav = input('Digite algo:')
print('O que foi digitado: {}'.format(palav))
print('O tipo primitivo desse valor é: {}'.format(type(palav)))
print('Só tem espaços? {}'.format(palav.isspace()))
print('É um numero? {}'.format(palav.isnumeric()))
print('É alfabético? {}'.format(palav.isalpha()))
print('É alfanumérico? {}'.format(palav.isalnum()))
print('Está em maiúsculo? {}'.format(palav.isupper()))
print('Esta em minúsculo? {}'.format(palav.islower()))
print('Esta capitalizado? {}'.format(palav.istitle()))