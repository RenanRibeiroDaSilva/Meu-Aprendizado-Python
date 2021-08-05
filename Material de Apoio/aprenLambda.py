contador_letras = lambda lista_palvras: [len(x) for x in lista_palvras]

lista_animais = ['gato', 'cachorro', 'papagaio', 'pinguin']
print(contador_letras(lista_animais))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
subt = calculadora['subtracao']
mult = calculadora['multiplicacao']
divi = calculadora['divisao']

print(soma(8, 9))
print(subt(87, 32))
print(mult(34, 23))
print((divi(9283, 33)))
