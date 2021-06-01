"""Ex 016 - Crie um programa que leie um número real e mostre na tela sua porção inteira"""

# Adicionando Blibliotecas
import math

print('-' * 15, '>Ex 16<', '-' * 15)

# Criando variaveis e Recebendo dados
num = float(input('Digite um valor real: '))

# Processando dados e Imprimindo na tela do usuario
print('O valor digitado foi {} e seu valor inteiro é {}'.format(num, math.trunc(num)))
