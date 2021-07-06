"""         Ex - 082 - Crie um programa que vai ler vários números e colocar em uma lista.
                        Depois disso, crie duas listas extras que vão conter apenas os valores
                        pares e os valores ímpares digitados, respectivamente. Ao final, mostre
                        o conteúdo das três listas geradas."""

#               Como eu fiz

# Lista:
numero = []
impare = []
pare = []

# Recebendo dados do usuario:
while True:
    numero.append(int(input('Digite um valor: ')))

    # Sair do laço de repetição:
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

# Separando valores na respectivas listas:
for n in numero:
    if n % 2 == 0:
        pare.append(n)
    else:
        impare.append(n)

# Imprimindo na tela para o usuário:
print('%-' * 30)
print(f'{numero} foram os números digitados!')
print(f'{pare} foram os números pares digitados!')
print(f'{impare} foram os números ímpares digitados!')

#       Como o Guanabara fez.
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista compreta é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {ímpares}')
