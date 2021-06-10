"""         Ex - 049 - Refaça o desafio 009, mostrando a tabuada de um número que o usuário
                        escolher, só que agora utilizando um laço for."""

#       Como eu fiz

n = int(input('Digite um número: '))
for t in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, t, n * t))

#   Como o Professor Guanabara Fez
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
