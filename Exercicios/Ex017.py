'''Ex 017 - Faça um programam que leia o comprimento do cateto oposto e do cateto adjecente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

print('-' * 15, '>Ex 17<', '-' * 15)

from math import hypot

cate_opos = float(input('Digite o valor do cateto oposto...:'))
cate_adje = float(input('Digite o valor do cateto adjecente:'))
hipo = hypot(cate_opos, cate_adje)

print('O valor da hipotenusa equivale há:{:.2f}'.format(hipo))
