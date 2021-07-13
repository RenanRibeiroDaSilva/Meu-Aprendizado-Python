"""         Ex - 092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
            (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
            também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
            a pessoa vai se aposentar.
"""

#           Como eu fiz

# Módulo:
from datetime import date


# T.L.D.:
pessoa = dict()

# Var:
hoje = date.today().year
pessoa['Nome'] = str(input('Nome: ')).strip().title()
pessoa['Ano_nasc'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho: '))
if pessoa['CTPS'] != 0:
    pessoa['Ano_contr'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposent'] = (pessoa['Ano_contr'] + 35) - pessoa['Ano_nasc']


print(f'{">DADOS CADASTRAIS<":-^50}')
print(f'Nome................: {pessoa["Nome"]}')
print(f'Idade...............: {hoje - pessoa["Ano_nasc"]} anos')
print(f'Carteira de trabalho Nº: {pessoa["CTPS"]}')
if pessoa['CTPS'] != 0:
    print(f'Ano de contratação..: {pessoa["Ano_contr"]}')
    print(f'Salário.............: R${pessoa["Salário"]}')
    print(f'Aposentadoria.......: {pessoa["Aposent"]}')
print(f'{"":-^50}')
print(f'{"FIM":_^50}')

#           Como o Guanabara fez.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem ): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')