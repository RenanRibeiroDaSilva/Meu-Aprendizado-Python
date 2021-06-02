"""     Ex - 031 - Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem,
                    cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

#               Como eu Fiz

# Receber e Criar uma varivel com o valor dado pelo usuário
km = int(input('Quanto Km de distância terá a sua viagem? '))

if km <= 200:
    print('O valor da sua passagem é de R${:.2f}'.format(km * 0.50))
else:
    print('O valor da sua passagem é de R${:.2f}'.format(km * 0.45))
print('--Fim--')

#       Como o professor Guanabara fez
distância = float(input('Qual é a distância da sua viagem?'))
print('Você está pretes a começar uma viagem de {}Km.'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45 #if simplificado
print('E o preço da sua passagem será de R${:.2f}'.format(preço))



