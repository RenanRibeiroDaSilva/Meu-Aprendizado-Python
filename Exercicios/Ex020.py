'''Ex 020 - O mesmo professor do desafio 19 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
a ordem sorteada'''

print('-' * 15, '>Ex 20<', '-' * 15)

# Importando biblioteca
from random import shuffle

# Recebendo dados
n1 = str(input('Qual nome do primeiro aluno:'))
n2 = str(input('Qual nome do segundo aluno:'))
n3 = str(input('Qual nome do terceiro aluno:'))
n4 = str(input('Qual nome do quarto aluno:'))

# Criando um array para armazena informações.
lista = [n1, n2, n3, n4]

# Criando a ordem selecionada
shuffle(lista)

# Imprimindo dados na tela para o usuario
print('A ordem de apresentação do trabalho será:')
print(lista)



