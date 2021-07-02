"""         Ex - 077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
                        Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

#               Como eu fiz.

# Tupla:
words = ('areia', 'batata', 'ostra', 'abelha',
         'caminhao', 'foguete', 'mexilhao',
         'planeta', 'estrela', 'bola', 'pe',
         'orelha', 'carreira', 'paralelepipedo')

print('-'*40)
print(f'{"SÓ VOGAIS":^40}')
print('-'*40)

for w in words:
    print(f'\n{w.upper():-<30}', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(f'{letter:>2}', end='')
print('\n')
print('-'*40)
