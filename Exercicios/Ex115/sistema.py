from Ex115.lib.interface import *
from time import sleep

cabecalho('SISTEMA ARQUIVO v1.0')

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opc1')
    elif resposta == 2:
        cabecalho('Opc2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)