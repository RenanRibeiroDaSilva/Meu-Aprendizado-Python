"""Ex 014 - Escreva um programa que converta uma remperatura digitando em graus Celcius
e conveta para graus Fahrenheit."""

print('-' * 15, '>Ex 14<', '-' * 15)

# Crindo variaveis e recebendo dados
gc = float(input('Qual á temperatura em Graus Ceulcius:'))
gf = ((gc * 9) / 5) + 32

# Processando e imprimindo dados na tela para o usuário.
print('{:.1f}°C equivale a {:.1f}°F'.format(gc, gf))
