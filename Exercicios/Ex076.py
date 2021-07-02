"""             Ex - 076 -  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
                            na sequência. No final, mostre uma listagem de preços, organizando os dados em forma
                            tabular.
"""

#               Como eu fiz

lista =('Arroz 5kg', 9.90, 'Feijão 1kg', 6.20,
        'Farinha de trigo', 2.35, 'Macarrão', 1.15,
        'Shampoo', 5.40, 'Sabonete', 0.35,
        'Pasta de dente', 1, 'Achocolatado em pó', 5.30,
        'Leite condensado', 3.30, 'Creme de leite', 2.10,
        'Mantega', 5.50, 'Requeijão', 3,
        'Banana 1k', 10, 'Maçã', 9)

print('~'*40)
print(f'{"LISTA DE COMPRAS":^40}')
print(f'{"":~^40}')
for inde in range(0, len(lista)):
    if inde % 2 == 0:
        print(f'{lista[inde]:.<33}', end='')
    else:
        print(f'R${lista[inde]:>5.2f}')
print('-'*40)