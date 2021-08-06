"""     Ex - 110 -  Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
        moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro
        pacote e mantenha tudo funcionando.
"""

from Ex111.utilidades import moeda

# Programa principal:
val = float(input('Digite um valor: R$'))

# Imprimir na tela para o usuário:
moeda.resumo(val, 32, 22)
