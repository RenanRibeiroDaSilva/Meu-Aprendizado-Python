"""         Ex - 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
                        pessoas não atingiram a maioridade e quantas já são maiores."""

#           Como eu Fiz

# Importar modulo:
from datetime import date

# Cabeçalho:
print(f'{"":=^40}')
print(f'{"Maior e Menor Idade":=^40}')
print(f'{"":=^40}')

# Var:
nasci = 0
maior = 0
menor = 0
atual = date.today().year

# Laço de Repetição:
for i in range(1, 8):
    nasci = int(input('Digite o ano de nacimento da {}° pessoa: '.format(i)))
    if atual - nasci >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo temos {} pessoa(s) maior(es) de idade.'.format(maior))
print('E temos {} pessoa(s) menor(es) de idades.'.format(menor))

#        Como o professor Guanabara Fez
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
'''
