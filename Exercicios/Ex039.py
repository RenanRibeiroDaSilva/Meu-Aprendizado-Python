"""         Ex - 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
                        com sua idade:
                        - Se ele ainda vai se alistar ao serviço militar.
                        - Se é a hora de se alistar.
                        - Se já passoi do tempo do alistamento.

                        Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""

#                Como eu Fiz
"""
# importar um modulo para ter a data atual
from datetime import date

# Criar um var para receber o dados do usuário
ano_nascimento = int(input('Em que ano você nasceu? '))

# Resolução do calculos matemáticos
data_de_hoje = date.today()
ano_atual = data_de_hoje.year
idade = ano_atual - ano_nascimento


# Impriminos os dados para o usuário
if idade == 18:
    print('Você está com {} e deve fazer seu alistamento militar'.format(idade))
elif idade > 18:
    print('Você está com {} e seu alistamento deveria ter sido feito a {} anos atrás'.format(idade, idade - 18))
elif idade < 18:
    print('Você está com {} e seu alistamento deverá ser realizad daqui {} ano(s)'.format(idade, 18 - idade))"""


#           Como o Professor Guanabara Fez
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alisatamento será em {} ano.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistameto foi em {} ano.'.format(ano))