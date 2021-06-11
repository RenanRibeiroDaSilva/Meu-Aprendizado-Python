"""         Ex - 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
                        desconsiderando os espaços.
                        Ex: APOS A SOPA
                        A SACADA DA CASA
                        A TORRE DA DERROTA
                        ANOTARAM A DATA DA MARATONA"""

#           Como o professor Guanabara fez
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # macete do fatiamento
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')

