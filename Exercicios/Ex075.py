"""             Ex - 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
                            No final, mostre:
                            A) Quantas vezes apareceu o valor 9.
                            B) Em que posição foi digitado o primeiro valor 3.
                            C) Quais foram os números pares.
"""

#               Como eu fiz

# Var:
num9 = pri3 = pos = pri = par = 0
num = ()


for n in range(1, 5):
    nu = int(input(f'Digite o {n}° valor: '))
    if n == 1:
        nu1 = nu
    else:
        if n == 2:
            nu2 = nu
        elif n == 3:
            nu3 = nu
        else:
            nu4 = nu

    if nu == 9:
        num9 += 1
    if nu == 3:
        pri += 1

num = (nu1, nu2, nu3, nu4)

print(f'Os números digitados foram ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO número 9 apreceu {num9} vez(es)!')
if pri == 0:
    print(f'O número 3 não apreceu em nenhuma posição')
else:
    for pos, pri3 in enumerate(num):
        if pri3 == 3:
            print(f'O número 3 apareceu ná {pos + 1}° posição')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('é(são) número(s) par(es)!')


#           Como o Guanabara fez
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')),)
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
