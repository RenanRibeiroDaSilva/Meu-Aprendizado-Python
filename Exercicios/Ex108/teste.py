""" Ex - 108 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
        números como um valor monetário formatado.
"""

import moeda

# Programa principal:
val = float(input('Digite um valor: R$'))

# Imprimir na tela para o usuário:
print(f'{moeda.moeda(val)} com 10% de taxa de juros tem o valor final de: {moeda.moeda(moeda.aumentar(val, 10))}')
print(f'{moeda.moeda(val)} com 10% de desconto tem o valor final de.....: {moeda.moeda(moeda.diminuir(val, 10))}')
print(f'O dobro de {moeda.moeda(val)} é.................................: {moeda.moeda(moeda.dobro(val))}')
print(f'A metade de {moeda.moeda(val)} é ...............................: {moeda.moeda(moeda.metade(val))}')
