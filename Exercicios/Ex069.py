"""         Ex - 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
                        o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
                        A) quantas pessoas tem mais de 18 anos.
                        B) quantos homens foram cadastrados.
                        C) quantas mulheres tem menos de 20 anos.
"""

#           Como eu fiz

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> CADASTRO <":~^50}')
print(f'{"":=^50}')

# Var:
cont_man = cont_mai18 = cont_mul_men20 = 0

# Programa:
while True:
    idade = int(input('Qual a idade: '))
    if idade > 18:
        cont_mai18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo: [M/F] ')).upper().strip()[0]

    if sexo in 'Mm':
        cont_man += 1

    if sexo in 'Ff' and idade < 20:
        cont_mul_men20 += 1

    contin = ' '
    while contin not in 'SsNn':
        contin = str(input('Quer continuar: [S/N]')).upper().strip()[0]

    print(f'{"":-^50}')
    if contin in 'Nn':
        break
print(f'Foram cadastrado(s) {cont_mai18} pessoa(s) com mais de 18 anos de idade!')
print(f'Foram cadastrado(s) {cont_man} homem(s)!')
print(f'Foram cadastrada(s) {cont_mul_men20} mulher(es) com menos de 20 anos de idade!')
print(f'{"-FINALIZANDO PROGRAMA DE CADASTRO-"}^50')