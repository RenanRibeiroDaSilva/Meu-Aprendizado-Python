"""     Aula - 019 - Diconários!"""

# Teórico:
'''
Variávei compostas (Diciónarios):
Diciónarios -> Estruturas compostas semalhantes as tuplas e a listas mas com a possibilidade ter ter
                indices literais.
Para declarar: 
    Tuplas = ( )
    Listas = [ ]
    Dicion = { }
Também podemos declarar desta forma:
    dados = dict()
    dados = {'nome':'Pedro', 'idade':25}
    print(dados['nome']     =  Pedro
    print(dados['idade']    =  25
Para adicionar elementos:
    dados['sexo'] = 'M' 
            |        |
            |         -----> Coloca o valor dentro da nova indexização que foi criada: {'sexo':'M'}
             --------------> Cria uma indexização chamada 'sexo'
Para renover elementos:
    del dados['idade'] ----> Deleta a indexização 'idade' e todos os seu valores.
    
Outra maneira de criar um diciónari:
    filme = {'titulo':'Star Wars',
             'ano':'1977',
             'diretos':'George Lucas'
             }
    
    -------------------------------------
    |'Strar Wars' | 1977 | 'George Lucas| --------
    -------------------------------------        |
      'titulo'      'ano'   'diretor'            |
                                                  -> Como ficara gravado na memória!
 
 Alguns comandos:
    print(filme.values()) ------------>  Vai me retornar todos os valores que estão no dicionário:
                                            'Star Wars', 1997, 'George Lucas'
    print(filme.keys()) -------------->  Vai me retornar todas a indexizações estão no dicionário:
                                               'titulo', 'ano', 'diretor'
    print(filme.items()) ------------->  Vai me retornar o dicionario inteiro com as valores e as keys:
    
Em um laço for:
    for k, v in filme.items():
        print(f'O {k} é {v}) --------->  O titulo é Star Wars
                                         O ano é 1977
                                         O diretor é George Lucas                                          
'''

# Prática:

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos')

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
print(pessoas.keys())

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
print(pessoas.values())

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
print(pessoas.items())

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
pessoas['nome'] = 'Nana'
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 28}
pessoas['peso'] = 88.90
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federatica: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
