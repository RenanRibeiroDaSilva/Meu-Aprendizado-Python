"""Ex 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma área de
2m²."""

print('-' * 10, '>Ex 011,', '-' * 10)

#Criando variaveis e recebendo dados.
par_alt = float(input('Qual a altura da parede: '))
par_lar = float(input('Qual a largura da parede: '))

#Processando dados.
area = par_alt * par_lar
tin = area / 2

#Imprimindo dados na tela para o usuário.
print('Sua parede tem a dimensão de {:.2f}X{:.2f} e sua área é de {:.2f}m².'.format(par_alt, par_lar, area))
print('Para pintar essa parede, voçê precisará de {:.2f}l de tinta.'.format(tin))
