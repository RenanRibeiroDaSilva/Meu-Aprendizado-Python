"""           Ex - 086 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo
                        teclado. No final, mostre a matriz na tela, com a formatação correta."""

#           Como eu fiz.

# Lista:
matr = [[], [], []]
num = 0

# Laço de repetição:
for n in range(0, 9):
    num = int(input(f'Digite o {n+1}ª valor: '))
    if n < 3:
        matr[0].append(num)
    elif 3 <= n <= 5:
        matr[1].append(num)
    else:
        matr[2].append(num)

print()
print(f'{"> MATRIZ <":^27}')
print('-' * 27)
for c in range(0, 3):
    print(f'[{matr[0][c]:^7}]', end='')
print()
for c in range(0, 3):
    print(f'[{matr[1][c]:^7}]', end='')
print()
for c in range(0, 3):
    print(f'[{matr[2][c]:^7}]', end='')
print()
print('-' * 27)

#       Como o Guanabara fez.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
