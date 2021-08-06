"""     Ex - 112 -  Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado
        dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
        mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from Ex112.utilidades import moeda
from Ex112.utilidades import dado

# Programa principal:
val = dado.leia_dinheiro('Digite um valor: R$')

# Imprimir na tela para o usuário:
moeda.resumo(val, 32, 22)
