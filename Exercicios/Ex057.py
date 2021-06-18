"""     Ex - 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
                    Caso esteja errado, peça a Digitação novamente até ter um valor correto."""

#           Como eu fiz.

# Cabeçalho:
print(f'{"":=^50}')
print(f'{"> Válidador de Genero <":=^50}')
print(f'{"":=^50}')

# Var:
genero = str(input('Informe seu genero [M/F]: ')).strip().upper()[0]

# Usar While para validar a operação:
while genero not in 'MmFf':
   genero = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: '))
print('Sexo {} foi cadastrado com sucesso!'.format(genero))

#       Como o Guanabara Fez.

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexi {} registrado com sucesso!'.format(sexo))