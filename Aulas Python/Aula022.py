"""         Aula - 022 - Módulos e Pacotes
"""

'''
    Modularização:
    -> Surgiu no início da década de 60.
    -> Sistemas ficando cada vez maiores.
    -> Foco: dividir um programa grande.
    -> Foco: aumentar a legibilidade.
    -> Foco: facilitar a manutenção.

'''

# Teoria:
'''
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c                                       -------------------uteis.py-----------------
    return f                                       |def fatorial(n):                          |  
                                                   |    f = 1                                 |  
                                                   |    for c in range(1, n+1):               |  
def dobro(n):                                      |        f*=c                              |  
    return n * 2                                   |     return f                             | 
                                                   | def dobro(n):                            |  
                                                   |    return n * 2                          |  
def triplo(n):                                     | def triplo(n):                           | 
    return n * 3                                   |    return n * 3                          |  
                                                   --------------------------------------------
                                                   ^ Criação de um módulo!
num = int(input("Digite um valor"))                
fat = fatorial(num)                                 
print(f"O fatorial de {num} é {fat}")           

Com o módulo uteis.py
import uteis

num = int(input("Digite um valor"))
fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')


            Vantagens de se usar modularização:
            -> Organização do código
            -> Facilidade na manutenção
            -> Ocutação de código detalhado
            -> Reutilização em outros projetos

>>> PACÓTES:
Junção de varios módulos, separados por assunto!    
'''
