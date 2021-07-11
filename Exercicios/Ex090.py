"""         Ex - 090 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
                        No final, mostre o conteúdo da estrutura na tela."""

#           Como eu fiz.

# Como eu fiz.

# Dicionário:
estru = {}
lista = []

# Loop:
while True:
    estru['nome'] = str(input('Qual nome do aluno? ')).strip().title()
    estru['n1'] = float(input(f'Qual a primeira nota do {estru["nome"]}: '))
    estru['n2'] = float(input(f'Qual a segunda nota do {estru["nome"]}: '))
    estru['média'] = (estru['n1'] + estru['n2']) / 2
    if estru['média'] >= 7:
        situ = 'Aprovado'
    elif 7 > estru['média'] >= 5:
        situ = 'Recuperação'
    else:
        situ = 'Reprovado'
    estru['situação'] = situ
    lista.append(estru.copy())
    estru.clear()
    resp = str(input('Quer conitunar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-*' * 15, '>BOLETIM<', '-*' * 15)
print(f'{"Nome":.<13}{"Média":.<8}{"Situção":.>8}')
for i, v in enumerate(lista):
    print(f'{lista[i]["nome"]:.<13}{lista[i]["média"]:.<8}{lista[i]["situação"]:.>8}')
print('=' * 32)

#           Como o Guanabara fez.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(f'Média de {aluno["nome"]}: ')
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['situação'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
