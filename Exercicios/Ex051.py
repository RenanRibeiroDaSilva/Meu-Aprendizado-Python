"""         Ex - 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
                        final, mostre os 10 primeiros termos dessa progressão."""

#           Como eu fiz
'''
# Cabeçalho:
print(f'{"":=^40}')
print(f'{"10 TERMOS DE UMA PA":^40}')
print(f'{"":=^40}')

# Variaveis:
n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão.........: '))
n3 = n1 * 20
if n1 == 0:
    n3 = 20

# Criar laço de repetição:
for c in range(n1, n3, n2):
    print(c, end=' ->')
print('Acabou')
'''

#       Como o Professor Guanabara fez
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ->')
print('ACABOU')
