"""         Ex - 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
        dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

import moeda

# Programa principal:
val = float(input('Digite um valor: R$'))

# Imprimir na tela para o usuário:
print(f'R${val} com 10% de taxa de juros tem o valor final de: R${moeda.aumentar(val, 10)}')
print(f'R${val} com 10% de desconto tem o valor final de.....: R${moeda.diminuir(val, 10)}')
print(f'O dobro de R${val} é.................................: R${moeda.dobro(val)}')
print(f'A metade de R${val} é ...............................: R${moeda.metade(val)}')
