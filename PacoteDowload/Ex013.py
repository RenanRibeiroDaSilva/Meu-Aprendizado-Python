"""Ex 013 - Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento."""

print('-' * 10, '>Ex 013,', '-' * 10)

# Criando variaveis e recebendo dados.
sal_func = float(input('Digite o valor do salário do funcionario: R$'))

# Processando dados.
val_aum = 0.15
novo_sal_func = sal_func + (sal_func * val_aum)

# Imprimindo dados na tela do usuário.
print('O salario do colaborado é de......: R${:.2f}'.format(sal_func))
print('O salario teve um aumento de......: {:.0f}%'.format(val_aum * 100))
print('O valor do salário atualizado é de: R${:.2f}'.format(novo_sal_func))
