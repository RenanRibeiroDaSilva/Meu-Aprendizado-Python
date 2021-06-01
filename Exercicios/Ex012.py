"""Ex 012 - Faça um algoritimo que leia  o preço de um produto e mostre seu novo preço,
com 5% de desconto."""

print('-' * 10, '>Ex 012,', '-' * 10)

#Criando variáveis e recebendo dados.
val_pro = float(input('Qual valor do produto: R$'))
desc = 0.05
novo_val_pro = val_pro - val_pro * desc

#imprimindo dados para o usuário na tela.
print('O valor do produto é de........: R${:.2f}'.format(val_pro))
print('O desconto dado é equivalente a: {:.0f}%'.format(desc * 100))
print('O valor final do produto é de..: R${:.2f}'.format(novo_val_pro))