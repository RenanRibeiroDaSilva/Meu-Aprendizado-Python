"""             Ex - 072 - Crie um progama que tenha uma tupla totalmente preenchida com uma contagem por extenso,
                            de zero até 20.
                            Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""

#           Como eu fiz.

# Tupla:
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezeseis',
            'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

# Var:
while True:
    while True:
        index = int(input('Digite um número entre 0 e 20: '))
        if 0 <= index <= 20:
            break
    print(f'Você digitou o número {contagem[index]}')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if res == 'N':
        break
print('FIM')