"""         Ex - 084 - Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
                        guardando tudo em uma lista. No final, mostre:
                        A) Quantas pessoas foram cadastradas.
                        B) Uma listagem com as pessoas mais pesadas.
                        C) Uma listagem com as pessoas mais leves."""

#               Como eu fiz.

# Listas:
pessoas = []
dados = []
maior = menor = 0

# Loop infinito:
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('_' * 40)
print(f'Foram cadastradas {len(pessoas)} pessoa(s)!')
print(f'A(s) pessoa(s) mais pesada(s) tinha(m) {maior}Kg. E é(são) ela(s) ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'A(s) pessoa(s) mais pesada(s) tinha(m) {menor}Kg. E é(são) ela(s) ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')

#           Como o Guanabara fez
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')
print()
