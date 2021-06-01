"""     Ex - 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela
                    cada um dos digitos separados.
                    Ex:
                    Digite um número: 1834
                    unidade: 4 dezena:3 centena:8 milhar:1"""

# Desta forma nos conceguiremos efetuar o programa desde que o usuário utilize números compostos por quatro digitos
# caso contrario o programa dará um erro e não concluira a aplicação.

# num = int(input('Informe um número:'))
# n   = str(num)
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena.: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar.: {}'.format(n[0]))

# Desta forma conseguiremos efetuar a aplicação independente de quantas casas o número desejado tenha em sua composição

num = int(input('Informe um número:'))
u   = num // 1 % 10         # Aquo fazemos uso da matemática para obter o resultado desejado. Pegamos o número
d   = num // 10 % 10        # dividimos pela unidade desejada (unidade dividimos pro 1, centena dividimos por 100)
c   = num // 100 % 10       # e ao buscarmos buscarmos o denominador desta divisão, encotraremos o resultado desejado.
m   = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena.: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar.: {}'.format(m))

