"""     Ex - 109 - Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
     desafio 108.
"""

import moeda

# Programa principal:
val = float(input('Digite um valor: R$'))

# Imprimir na tela para o usuário:
print(f'{moeda.moeda(val)} com 10% de taxa de juros tem o valor final de: {moeda.aumentar(val, 10, True)}')
print(f'{moeda.moeda(val)} com 10% de desconto tem o valor final de.....: {moeda.diminuir(val, 10, True)}')
print(f'O dobro de {moeda.moeda(val)} é.................................: {moeda.dobro(val, True)}')
print(f'A metade de {moeda.moeda(val)} é ...............................: {moeda.metade(val, True)}')
