"""     Aula - 010 - Condições Simples e Compostas: Nesta aula vamos aprender como ultilizar estruturas
                    condicionais simples e compostas nos programas em Python."""


# Fase Teórica
# Aqui aprendemos o uso do if else, e como contruir a sua identação.
# if variavel.ação_desejada():
#   bloco True
# else:
#   bloco False


#Ex:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')


# Condição Simplificada.
# No caso de condições simples.
# Ex:
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')


# Fase prática.
# Prática 1.
nome = str(input('Qual é seu nome? ')).upper()
if nome == 'RENAN':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome.title()))


#Pratica 2.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota.: '))
n  = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(n))
if n >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média fou ruim! ESTUDE MAIS!')

# ou usando condição simplificada
print('PARABÉNS!' if n >= 6.0 else 'ESTUDE MAIS!')
