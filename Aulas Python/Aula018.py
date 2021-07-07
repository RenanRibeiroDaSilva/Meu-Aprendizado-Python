"""         Aula - 018 - Listas(parte 2)"""

# Variáveis compostas (listas) parte 2:
# Teoria:
'''
Lista dentro de lista:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] # Aqui colocamos listas dentro de uma única lista.

Buscas dentro da lista:
print(pessoas[0][0]) # Aqui será encontrado o valor dentro da endexização zero, na indexização zero.
        |
        --------> Pedro
print(pessoas[1][1])
        |
        --------> 19
print(pessoas[2][0])
        |
        --------> João
print(pessoas[1])
        |
        --------> ['Maria', 19]
'''

# Prática:

teste = list()
teste.append('Renan')
teste.append(28)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['Renan', 28], ['Ana', 33],['Joaquim', 13], ['Maria' ,45]]
# print(galera[1][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')


galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
