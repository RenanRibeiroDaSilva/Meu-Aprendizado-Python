"""         Ex - 042 - Refaça o DESAFIO 035 dos triângulos, acresentando o recurso de mostrar que tipo
                        de triãngulo será formado:
                        - Equilátero: todos os lados iguais
                        - Isósceles: dois lados iguais
                        - Escaleno: todos os lados diferentes"""

#           Como eu Fiz

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento.: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acime não podem formar um triângulo!')

# Criar condicional mostrar o resultado desejado ao usuário.

if r1 == r2 and r2 == r3:
    print('Equilátero: todos os lados iguais')
elif r1 != r2 and r2 != r3 and r3 != r1:
    print('Escaleno: todos os lados diferentes')
else:
    print('Isósceles: dois lados iguais')

#   Como o professor Guanabara fez

print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento.: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima podem formar um triângulo!', end='')
    if r1 == r2 == r3:
        print('EQUILATÉRO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acime não podem formar um triângulo!')
