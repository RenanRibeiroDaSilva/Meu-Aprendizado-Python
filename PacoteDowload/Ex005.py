"""Ex 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor."""

#Recebendo dados
n1 = int(input('Digite um valor:'))
num_ant = n1 - 1
num_suc = n1 + 1

#Processando dados e imprimindo na tela
print('Analisando o valor {}, seu sucessor é {} e seu antecessor é {}.'.format(n1, num_suc, num_ant))
