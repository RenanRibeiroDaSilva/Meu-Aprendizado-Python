"""Ex 008 - Escreva um programa que que leia um valor em metros e o exiba convertido em
centímetros e milímetros"""

print('=' * 10, '>Ex008<', '=' * 10)

#Recebendo dados
n1 = float(input('Quantos metros gostaria de converter? '))

#Processando dados
km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
dm = n1 * 10
cen = n1 * 100
mili = n1 * 1000

#Imprimindo dados na tela para o usuario
print(' {:.0f}m equivale a {}Km'.format(n1, km))
print(' {:.0f}m equivale a {}hm'.format(n1, hm))
print(' {:.0f}m equivale a {:.1f}dam'.format(n1, dam))
print(' {:.0f}m equivale a {:.0f}dm'.format(n1, dm))
print(' {:.0f}m equivale a {:.0f}cm'.format(n1, cen))
print(' {:.0f}m equivale a {:.0f}mm'.format(n1, mili))
