"""         Ex - 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
            retangular (largura e comprimento) e mostre a área do terreno."""

#           Como eu fiz.


def area(lar, com):
    are = lar * com
    print(f'Um terrreno com {lar:2.2f}m X {com:2.2f}m tem uma área de {are:5.2f}m²')


def cabe():
    print(f'{"":=^60}')
    print(f'{">Área do Terreno<":^60}')
    print(f'{"":=^60}')


# Programa pricipal:
cabe()
a = float(input('Qual a largura do terreno: '))
b = float(input('Qual o comprimento do terreno: '))
area(a, b)

#           Como o Guanabara fez.


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos.')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
