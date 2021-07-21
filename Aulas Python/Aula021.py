"""         Aula - 021 - Funções(parte 2)."""

# Temas que serão abordados nesta aula:
'''
> Interactive Help.
> docstrings.
> Argumentos opcionais.
> Escopo de variáveis.
> Retorno de resultados.
'''

# Teoria:
'''
>>> Interactive Help: 
    Muitas linguagem de programação tem seus manuais para auxiliar no desenvolvimento do programador.
No Python, caso o usuário necessite ele pode usar o camando help() ou print(algumacoisa.__doc__) que 
o proprio Python vai tentar auxilia-lo com as duvidas á respeito do comando questionado.

>>> docstrings:
    Cria um manual que vai ser exibido em um help().

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por Gustavo Guanabara do CursoemVídeo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

>>> Argumentos opcionais:
    Podemos da parametros preestabelecidos para as variaveis quando ciramos uma função como mostra o 
exemplo a baixo. Assim, caso o usuario não declare a variavel c por exemplo, a função não dara erro.

def somar(a=0, b=0, c=0):
    """ 
    -> Faz a soma de três valores e mostra  o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """
    s = a + b + c
    print(f'A soma vale{s}')
    

somar(3, 2, 5)
somar(8, 4)
somar()

>>> Escopo de variáveis:
    Local onde uma vareável vai existir.
    Caso eu queira alterar o valor de alguma vareável global dentro de uma função é necessarios usar 
o termo global varialvel.

>>> Retorno de resultados:
return -> retorna um valor!
'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')
