"""         Aula - 015 - Interrompendo repetições com o While"""

# Laços de repetição (parte 3):
'''
Enquanto Veridadeiro      | while True:
    se chão               |     if chão:
        pesso             |         passo
    se espaço vazio       |     if vazio:
        pula              |         pula
    se moeda              |     if moeda:
        pega              |         pega
    se trofeu             |     if trofeu:
        pula              |         pula
        interrompa        |         break
pega                      | pega
'''

# Parte prática da aula:
# LAço infinito.
'''
cont = 1
while True:
    print(cont, '--> ', end='')
    cont += 1
print('Acabou')'''

# laço infinito com break:
'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if  n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
'''

