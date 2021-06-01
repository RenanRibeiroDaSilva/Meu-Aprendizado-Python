"""Ex 015 - Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60,00 por dia e R$0,15 por Km rodado."""

print('-' * 15, '>Ex 15<', '-' * 15)

# Criando variaveis e Recebendo dados.

dia_car = int(input('Por quantos dias você alugou o carro: '))
km_rodado = float(input('Quantos KM foram rodados: '))

# Processando dados.
val_dia_car = dia_car * 60
val_km_rodado = km_rodado * 0.15
total_pag = val_dia_car + val_km_rodado

# Imprimindo dados para o usuário.
print('Valor a pagar pelos dias......: R${:.2f}'.format(val_dia_car))
print('Valor a pagar pelos KM rodados: R${:.2f}'.format(val_km_rodado))
print('Valor total a pagar...........: R${:.2f}'.format(total_pag))