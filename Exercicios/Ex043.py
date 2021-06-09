"""     Ex - 043 - Desenvolva uma lógica que leia o peso e a aultura de uma pessoa, calcule seu IMC e mostre
                    seu status, de acordo com a tabela abaixo:
                    - Abaixo de 18.5: Abaixo do peso
                    - Entre 18.5 e 25: Peso ideal
                    - 25 até 30: Sobrepeso
                    - 30 até 40: Obesidade
                    - Acima de 40: Obesidade mórbida"""

#               Como eu Fiz

# Importar modulo
from math import pow

# Criar variaveis:
peso = float(input('Qual seu peso atul...: '))
altu = float(input('Qual sua altura......: '))

# Resoluções matemáticas:
imc = peso / pow(altu, 2)
print('Seu IMC é igual há {:.1f}, e você é considerado '.format(imc), end='')

# Criar condicional para mostrar o resultado desejado ao usuário:
if imc <= 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print('PESO IDEAL!')
elif 25 < imc <= 30:
    print('SOBREPESO!')
elif 30 < imc <= 40:
    print('OBESO(a)!')
else:
    print('OBESO MORBIDO(a)!')

#       Como o professor Guanabara Fez

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você estpa em OBESIDADE!')
elif imc > 40:
    print('Você está em OBESIDADE MORBIDA, cuidado!')
