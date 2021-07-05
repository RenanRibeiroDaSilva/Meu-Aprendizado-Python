"""         Ex - 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
                        uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a
                        lista ordenada na tela."""

#       Como eu fiz.

# Lista:
numeros = list()

# Laço de repetição:
for i in range(0, 5):
    n = int(input(f'Digite o {i+1}° valor: '))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print(f'{n} adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            pos += 1
print('~~' * 20)
print(f'Os valores digitados foram {numeros}!')

#       Como o Guanabara fez
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
