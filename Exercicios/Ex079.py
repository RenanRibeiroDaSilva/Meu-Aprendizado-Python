"""         Ex - 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
                        uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
                        exibidos todos os valores únicos digitados, em ordem crescente.
"""

#           Como eu fiz.

# Lista:
lista_num = []

# Loop de repetição:
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista_num:
        print(f'Valor {valor} adicionando a lista.')
        lista_num.append(valor)
    else:
        print(f'Valor {valor} já está na lista, não vou adicionar novamente.')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont in 'N':
        break
print(sorted(lista_num))

#           Como o Guanabara fez
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
