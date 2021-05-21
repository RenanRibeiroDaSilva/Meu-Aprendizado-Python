"""Ex 007 - Desenvolva um programa que leia à duas nota de um aluna caulcule e mostre a sua média"""

print('=' * 10, ">Ex007<", "=" * 10)

#Recebendo dados
nota1 = float(input('Qual valor da primeira nota: '))
nota2 = float(input('Qual valor da segunda nota: '))

#Processando Dados
media = (nota1 + nota2) / 2

#Imprimindo Dados para o usuario
print('A média entre as notas {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, media))
