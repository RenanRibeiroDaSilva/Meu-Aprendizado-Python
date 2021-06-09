"""         Ex - 41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
                    atleta e mostre sua categoria, de acordo com a idade:
                      - Até 9 anos: MIRIM
                      - Até 14 anos: INFANTIL
                      - Até 19 anos: JUNIOR
                      - Até 20 anos: SÊNIOR
                      - Acima: MASTER """

#           Como eu Fiz
'''
# Criar variavel para receber a idade do atleta
idade = int(input('Qual a idade do atleta: '))

# Criar condicional para mostrar o resultado ao usuário
if idade <= 9:
    atleta = '\033[36mMIRIM\033[m'
elif 10 <= idade <= 13:
    atleta = '\033[34mINFANTIL\033[m'
elif 14 <= idade <= 18:
    atleta = '\033[32mJUNIOR\033[m'
else:
    atleta = '\033[7;30;47mSÊNIOR\033[m'
print('O atleta tem {} anos e está classificado como atleta {}!'.format(idade, atleta))
'''

#     Como o Professor Guanabara Fez

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
