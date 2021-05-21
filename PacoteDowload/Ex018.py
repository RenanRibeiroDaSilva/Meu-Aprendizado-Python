'''Ex 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.'''

print('-' * 15, '>Ex 18<', '-' * 15)

from math import tan, cos, sin, radians

ag = float(input('Digite o valor do angulo: '))

radi = radians(ag)
seno = sin(radi)
cose = cos(radi)
tang = tan(radi)

print('{:.2f} é o seno, {:.2f} é o coseno e {:.2f} é a tangente um angulo de {:.1f}G°'.format(seno, cose, tang, ag))
