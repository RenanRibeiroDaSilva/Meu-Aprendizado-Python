"""         Ex - 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
            pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
            A) Quantas pessoas foram cadastradas
            B) A média de idade
            C) Uma lista com as mulheres
            D) Uma lista de pessoas com idade acima da média
"""

#       Como eu fiz.

# T.L.D.:
dados = dict()
cadas = list()

# Area de desenvolvimento:
while True:
    # Recebendo informações:
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Por favor digite uma das opções dadas [M/F]: ')

    dados['idad'] = int(input('Idade: '))
    # Alocando dados na lista cadas:
    cadas.append(dados.copy())
    # Limpando dicionário para novos dados:
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Codigo incorreto! Selecione entre S ou N: ')
    if resp in 'N':
        break
print(f'{">BANCO DE DADOS<":¨^60}')
# Imprimindo na tela o tatal de pessoas cadastradas:
print(f'{"Total de Cadastros:":.<20}{len(cadas):.>38.2f}')
# Imprimindo na tela a média de idade das pessoas cadastradas:
soma = 0
for i, v in enumerate(cadas):
    soma += cadas[i]['idad']
media = soma / len(cadas)
print(f'Média de idade:{"":.<20}{media:.>23.2f}')
# Imprimindo somente as mulheres cadastradas:
print(f'{">Mulheres Cadastradas<":-^60}')
for d, v in enumerate(cadas):
    if cadas[d]['sexo'] in 'F':
        print(f'{cadas[d]["nome"]:^60}')
# Imprimindo somente as pessoas com idade maior que a média das pessoas cadastradas:
print(f'{">Pessoas com idade acima da média<":-^60}')
for i, j in enumerate(cadas):
    if cadas[i]['idad'] > media:
        print(f'{cadas[i]["nome"]:^60}')
print(f'{"-Fim-":=^60}')

#       Como o Guanabara fez.
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas foram cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')
