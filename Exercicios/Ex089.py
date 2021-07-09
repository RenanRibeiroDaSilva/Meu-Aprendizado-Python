"""         Ex - 089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
            lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
            mostrar as notas de cada aluno individualmente."""

#           Como eu fiz

# Lista:
lisNot = list()
lisAlu = list()
lisMaj = list()

# Loop:
while True:
    lisAlu.append(str(input('Qual nome do aluno: ')).title())
    for n in range(0, 2):
        lisNot.append(float(input(f'Digite a {n+1}ª nota do(a) {lisAlu[-1]}: ')))
    lisAlu.append(lisNot[:])
    lisMaj.append(lisAlu[:])
    lisNot.clear()
    lisAlu.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('~' * 15, '>BOLETIM<', '~' * 15)
print(f'{"Nº":.<5}{"Nome":.^10}{"Média":.>26}')
for i in range(0, len(lisMaj)):
    print(f'{i+1:.<8}', end='')
    print(f'{lisMaj[i][0]:.<23}', end='')
    media = (lisMaj[i][1][0] + lisMaj[i][1][1]) / 2
    print(f'{media:.>10.1f}')

while True:
    print('-' * 41)
    aluno = str(input('Quer ver as notas de qual aluno: ')).strip().title()
    print('-' * 41)
    print(f'{"Aluno:":.<25}{"1ªNota:":<5}{"2ªNota:":>9}')
    for a in lisMaj:
        if aluno in a:
            print(f'{a[0]:.<25}', end='')
            print(f'{a[1][0]:>5.1f}', end='')
            print(f'{a[1][1]:>9.1f}')
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
print('*' * 41)
print('Fim do programa!!!')

#           Como o Guanabara fez.
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
