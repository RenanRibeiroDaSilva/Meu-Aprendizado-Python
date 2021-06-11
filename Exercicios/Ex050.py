"""         Ex - 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
                        daqueles que forem pares. Se o valor digitado for impar, desconsidere-o"""

#           Como eu Fiz

# Cabeçalho:
print(f'{"=":=^40}')
print(f'{"> Soma do números Pares<":=^40}')
print(f'{"=":=^40}')

# Variaveis:
soma = 0
count = 0

# Criar um laço de repetição:
for c in range(1, 7):
    # Receber dados do usuário:
    num = int(input('Digite um número: '))
    # Criar condicional:
    if num % 2 == 0:
        count = count + 1
        soma = soma + num
print('A soma de todos os {} números pares que eu recebi é {}'.format(count, soma))

#       Como o professor Guanabara Fez
cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números e a soma é {}'.format(cont, soma))
