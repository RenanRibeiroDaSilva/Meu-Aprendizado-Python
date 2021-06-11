"""         Ex - 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
                        maior e o menor pesos lidos."""

#           Como eu fiz

# Cabeçalho:
print(f'{"":=^40}')
print(f'{"> MAIOR PESO LIDO <":=^40}')
print(f'{"":=^40}')

# Var:
maior_peso = 0
menor_peso = 1000

# Laço de repetição:
for pess in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? (Kg) '.format(pess)))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('A pessoa com MAIOR PESO tem {:.1f}Kg'.format(maior_peso))
print('A pessoa com MENOR PESO tem {:.1f}Kg'.format(menor_peso))

#        Como o Professor Guanabara Fez
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(int('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior == peso
        menor == peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor < peso
print('O mairo peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))