"""         Ex - 085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
                        única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
                        ímpares em ordem crescente."""

#           Como eu fiz.

# Lista:
list_num = [[], []]
num = 0
# Laço de repetição:
for n in range(0, 7):
    num = int(input(f'Digite o {n+1}ª valor: '))
    if num % 2 == 0:
        list_num[0].append(num)
    elif num % 2 == 1:
        list_num[1].append(num)
print('-*' * 30)
list_num[0].sort()
print(f'Os números pares digitados foram {list_num[0]}')
list_num[1].sort()
print(f'Os números ínpares digitados foram {list_num[1]}')

#    Como o Guanabara fez.
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ínpares digirados foram: {núm[1]}')
