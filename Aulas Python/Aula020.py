"""         Aula - 020 - Funções em Python(parte 1).
"""

# Teórico:
'''
    Criar uma funão serve para facilitar tarefes que somos hábituados a fazer contantemente. E para não termos que 
escrever as mesmas linha de código várias vezes, podemos coloca-lo dentro de uma função personalidada por nós mesmos
e usa-la assim com print, int, float, input, etc. Que também são funções, porem já vem intregrado ao phyton por ser 
algo universal. 

def = definição de função.

    Exp:
    print('------------------------------------') }-|
    print('          SISTEMA DE ALUNOS         ')   |
    print('------------------------------------') }-|
    print('------------------------------------') }-|
    print('       CADASTRO DE FUNCIONÁRIOS     ')   |
    print('------------------------------------') }-|--------> O mesmo código escrito variaz vez!
    print('------------------------------------') }-|              temos uma uma Rotina!
    print('           ERRO DE SISTEMA          ')   |
    print('------------------------------------') }-|
    
    Podemos fazer uma função para mostrar esta linha sempre que desejarmos.
    
    def MostraLinha():
        print('------------------------------------')
    
    MostraLinha()                                 }-|
    print('          SISTEMA DE ALUNOS         ')   |
    MostraLinha()                                 }-|
    MostraLinha()                                 }-|
    print('       CADASTRO DE FUNCIONÁRIOS     ')   |
    MostraLinha()                                 }-|-------->  Usamos a função criada MostraLinha() e substituimos
    MostraLinha()                                 }-|              os códigos que se repetian!
    print('           ERRO DE SISTEMA          ')   |
    MostraLinha()                                 }-|
    
'''
# Passando parametros para funções:
'''
    Exp:
    def título(txt):
        print('------------------------------------') }-|
        print(txt)                                      |----->  Aqui nos estmaos definindo valores para as funções.
        print('------------------------------------') }-|
        
    # Programa principal
    título('    CURSO EM VÍDEO      ')
'''

# Prática:

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)

soma(b=4, a=5)
soma(7, 2)
'''

'''
def contador(* núm):
    for valor in núm:
        print(valor, end=' ')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
