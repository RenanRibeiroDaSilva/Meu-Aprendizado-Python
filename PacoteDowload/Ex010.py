"""Ex 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar."""

print('=' * 10, '>Ex010<', '=' * 10)

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real * 0.327


print('Você pode compra US${:.2f} com seus R${:.2f}'.format(dolar, real))