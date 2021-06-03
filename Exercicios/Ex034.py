"""     Ex - 0340 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor
                    do seu aumento.

                    Para salários superiores a R$1.250,00 calcule um aumento de 10%.

                    Para os inferiores ou iguais, o aumento é de 15%."""

#           Como eu Fiz

# Criar uma variavel para receber o valor do salário do usuário
salario = float(input('Qual o valor do salário do colaborador: R$'))

# Criar uma condição para efetuar o aumento com base no valor do salário
if salario <= 1250.00:
    aumento = 0.15
if salario > 1250.00:
    aumento = 0.10

salario_atualizado = salario + (salario * aumento)

# Mostrar para o usuário na tela
print('Seu salário era de........ R${:.2f}'.format(salario))
print('Seu aumento foi de........ {:.0f}%'.format(aumento * 100))
print('Seu salário atual é de.... R${:.2f}'.format(salario_atualizado))

#        Como o Guanabara fez

salário = float(input('Qual salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print('Quem ganhava R${:.2f} pessa a ganhar R${:.2f} agora'.format(salário, novo))
