"""         Ex - 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
                        No final, mostre qual foi o maior e o menor valor digitado e as suas
                        respectivas posições na lista."""


#             Como eu Fiz.

# Lista:
lista = []
for i in range(0, 5):
    valor = int(input(f'Digite um valor na posição {i}: '))
    lista.append(valor)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {max(lista)} nas posiçãos ', end='')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}...', end='')
print()
print(f'O menor valor foi {min(lista)} nas posiçãos ', end='')
for pos, v in enumerate(lista):
    if v == min(lista):
        print(f'{pos}...', end='')
print()

#         Como o Guanabara fez.
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas pisições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
