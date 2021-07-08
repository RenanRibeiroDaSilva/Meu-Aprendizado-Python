"""         Ex - 087 - Aprimore o desafio anterior, mostrando no final:
                        A) A soma de todos os valores pares digitados.
                        B) A soma dos valores da terceira coluna.
                        C) O maior valor da segunda linha.
"""

#           Como eu fiz.

# Lista:
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Var:
somaPar = somaTerCol = maior = 0

# Laço dentro de um laço:
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        somaTerCol += mat[l][2]
        if mat[l][c] % 2 == 0:
            somaPar += mat[l][c]
        if mat[1][c] == 0:
            maior = mat[l][c]
        else:
            if mat[1][c] > maior:
                maior = mat[1][c]

print('¨¨' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^7}]', end='')
    print()
print(f'A soma de todos os valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaTerCol}')
print(f'O maior valor da segunda linha é: {maior}')

#       Como o Guanabara fez
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    print('-=' * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if matriz[l][c] % 2 == 0:
                spar += matriz[l][c]
        print()
    print('-=' * 30)
    print(f'A soma dos valores pares é {spar}')
    for l in range(0, 3):
        scol += matriz[l][2]
    print(f'A soma dos valores da terceira coluna é {scol}.')
    for c in range(0, 3):
        if c == 0:
            mai = matriz[1][c]
        elif matriz[1][c] > mai:
            mai = matriz[l][c]
    print(f'O maior valor da segunda linha é {mai}.')
