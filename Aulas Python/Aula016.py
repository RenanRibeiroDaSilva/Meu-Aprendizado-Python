"""             Aula - 016 - Tuplas"""

# Teoria:

# Variáveis compostas:
'''
Tuplas, o que são?:
    Em uma explicação bem simples, é uma variável que guarda vários valores!
    As tuplas usam indexições para indentificar seu componentes internos!
    As tuplas são imultáveis!   
'''

# Parte prática:

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3], '\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi muito!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Estou farto!')

print(sorted(lanche))  # ------> sorted = organizar.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(2))

del (lanche)  # Uma tupla é imutável, mas podemos deletar ela inteira. Se tentarmos deletar apenas
# uma indexação ele dara erro.
