"""         Ex - 048 - Faça um programa que calcule a soma entre todos os números impares que
                        são múltipços de três e que se encotram no intervalo de 1 até 500"""

#   Como eu Fiz

print(f'{"> Soma Dos Números Multiploes de 3 <":=^40}')

# Criar laço de repetição
s = 0
for n in range(3, 501, 3):
    if n % 2 == 1:
        s = s + n
print(s)

#       Como o professor Guanabara fez
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
