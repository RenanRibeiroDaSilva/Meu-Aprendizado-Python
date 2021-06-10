"""     Aula - 013 - Estrutura de repetição for"""

''' Laços de Repetição (parte 1)

Parte teorica:

laço com variavel de controle.

Aqui o Professor Guanabara fez o uso de exemplos com laços de repetição para nos
mostrar como faze-lo no pytho!

laço c no intervalo(1,10)
    passo
pega

for c in range(1,10):
    passo
pega

Aqui ele fez uma pequena alteração no laço adicionando mais uma ação dentro do laço de repetição!

laço c no intervalo(0,3)
    passo
    pula
passo
pega

for c in range(0,3):
    passo
    pula
passo
pega

Agora vamos fazer o uso de estrutura de controle condicional

laço c intervalo(0,3)
    se tiver moeda
        pega
    passo
    pula
passo
pega

for c in range(0,3)
    if tiver moeda
        pega
    passo
    pula
passo
pega

Parte prática da aula:

for c in range(0, 7, 2):
    print(c)
print('-FIM-')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')
'''
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores da {}'.format(s))