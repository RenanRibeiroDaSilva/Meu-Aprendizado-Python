"""             Ex - 081 - Crie um programa que vai ler vários números e colocar em uma lista.
                Depois disso, mostre:
                A) Quantos números foram digitados.
                B) A lista de valores, ordenada de forma decrescente.
                C) Se o valor 5 foi digitado e está ou não na lista."""

#       Como eu fiz

# Lista:
lista_num = list()
c = 0
# Loop:
while True:
    num = int(input('Digite um valor: '))
    lista_num.append(num)
    c += 1
    res = str(input('Quer continuar? [S/N] ')).strip()[0]
    if res in 'Nn':
        break

print('~-' * 25)
print(f'Foram digitados {c} valores!')
lista_num.sort(reverse=True)
print(f'Os valores digitados foram {lista_num} em ordem drecesente!')
if 5 in lista_num:
    print(f'O número 5 foi digitado na lista!')
else:
    print('O número 5 não foi digitado!')

#       Como o Guanabara fez
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
