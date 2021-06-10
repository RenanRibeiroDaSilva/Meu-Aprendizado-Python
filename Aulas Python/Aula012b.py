"""         Aula - 012 - Condições Aninhadas"""

# Fase Teórica
'''
carro.siga()
se carro.esquerda():       = if carro.esquerda():
    carro.siga()                bloco 1
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão se carro.direita():  = elif carro.direita(): 
    carro.siga()                bloco 2
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senão:                     = else:
    carro.siga()                bloco 3
carro.pare()
'''

# Fase prática


nome = str(input('Qual é o seu nome? '))
if nome == 'Renan':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

