"""         Ex - 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
            parâmetro e mostre uma mensagem com tamanho adaptável.
            Ex:
            escreva(‘Olá, Mundo!’) Saída:
            ~~~~~~~~~
            Olá, Mundo!
            ~~~~~~~~~
"""


#               Como eu fiz.

# Criando função:
def escrevar(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Progama pricipal:
t = str(input('Digite uma frase: ')).strip().title()
escrevar(t)
# Fim do programa.


#            Como o Guanabara fez.
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa pricipal:
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')