"""     Aula  - 011 - Cores no terminal (Com o professor Gustavo Guanabara)"""


'''codigo ANSE
\033[0;33;44m]

style
0 none
1 bold
4 underline
7 negative

text               Back
30 branco          40
31 vermelho        41 
32 verde           42
33 amarelo         43
34 azul            44
35 roxo            45
36 azul piscina    46 
37 Cinza           47 


print('teste\033[0;30;41m')
print('teste\033[4;33;44m')
print('teste\033[1;35;43m')
print('teste\033[30;42m')
print('teste\033[m')
print('teste\033[7;30m')'''


print('\033[0;31;43mOlá, mundo\033[m')

a = 3
b = 5
print('Os valores são \033[34m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Renan'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))


nome = 'Renan'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
