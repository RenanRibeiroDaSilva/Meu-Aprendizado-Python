"""     Ex - 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
                     80Km/h, mostre uma mensagem dizendo que ele foi multado.
                     A multa vai custar R$7,00 por cada Km acima do limite."""


#                           Como eu Fiz

# Criar variavel para a velocidade do veículo
print('-=-' * 20)
print('BEM VINDO AO RADAR ELETÔNICO')
print('-=-' * 20)
vel_carro = float(input('Qual a velocidade do veículo? '))

vel_acima = vel_carro - 80
val_multa = vel_acima * 7

from time import sleep
print('Processando...')
sleep(2.5)

if vel_carro >80.00:
    print('-' * 60)
    print('Ele merecere uma multa por ultrapassar o limete de velocidade!')
    print('O valor da multa é de R${:.2f}'.format(val_multa))
    print('-' * 60)
else:
    print('-' * 60)
    print('PARABÉNS! Ele esta dentro do limite de velocidade!')
    print('-' * 60)



#               Como o professor Guanabara Fez

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você execeu o limite permitido que é 80KM/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

