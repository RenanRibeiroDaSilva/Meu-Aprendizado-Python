'''Ex 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

print('-' * 15, '>Ex 19<', '-' * 15)

from random import choice

# Usando Random para sortiar o escolhido.

# Recebendo dados.
aluno1 = str(input('Digite o nome do aluno:'))
aluno2 = str(input('Digite o nome do aluno:'))
aluno3 = str(input('Digite o nome do aluno:'))
aluno4 = str(input('Digite o nome do aluno:'))

# Criando um array para escolher um entre os informados.
lista = [aluno1, aluno2, aluno3, aluno4]

# Usando choice para sortiar um dentro do array.
escolhido = choice(lista)

# Imprimindo dados na tela para o usuario.
print('O escolhido foi {}'. format(escolhido))