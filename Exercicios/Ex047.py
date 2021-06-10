"""         Ex - 047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50"""

#   Como eu Fiz

print(f'{"> Números Pares <":=^40}')

# Criar var:
num_par = []


# Criar laço de repetição:
for count in range(1, 51):
    par = count % 2
    if par == 0:
        num_par.append(count)
print('{} Acabou'.format(num_par))

# Como o professor Guanabara fez
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
