"""            Aula - 014 - Estrutura de Repetição While (parte 2)."""

# Fase teórica.
''' Vimos as diferenças entre o while e o for.
    Chamamos o while de "Estrutura de repetição com teste lógico".
    Le-se "while" como "enquanto"
    
    enqunto não maça    | while not maçã:
        passo           |   passo
    pega                | pega
    
    while not maçã:
        if chão == v:
            passo
        if buraco == v:
            pular
        if moeda == v:
            pega
    pega
    '''

# Fase prática:
'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

'''n = 1
while n != 0: # Ponto de parada
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('Fim')'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))
'''
