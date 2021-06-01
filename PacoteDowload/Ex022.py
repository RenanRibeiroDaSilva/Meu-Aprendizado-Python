"""     Ex-022- Crie um programa que leia o nome completo de uma pessoa 
    e mostre:
    > O nome com todas as letras maiúsculas e minúsculas.
    > Quantas letras ao todo (sem considerar espaços).
    Quantas letras tem o primeiro nome."""

# Usamos .strip() para descartar espaços vazios antes e depois da string
nome = str(input('Digite seu nome completo: ')).strip()

# Usamos print para imprimir na tela para o usuario
print('Analizando seu nome...')

# Usamos upper() para colocar todas as letras em maiúsculas
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))

# Usamos lower() para colocar todas as letras em minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Usamos len() para saber o tamanho da string e count para contar os espaços vazio entre as palavar
# depois fizemos um subtração da quantidade de letras obtidas com o len() menos a quantidades de espaços
# vazios encontrados pelo count(' ')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# Usamos o find() para encontrar o primeiro espaço vazio neste caso e separar a primeira pralavra do restante da frase
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# Criamos um variavel separa e adicionamos o valor do nome com split() para descartar espaços vazios antes e depois
# da string
separa = nome.split()

# Usamos a variavel separa no valor zero para nos estregar apenas a palavra que inicia na posição zero e len() para
# encontra apenas o tamanho da paralava que está na posição zero.
print('Seu primeino nomé é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

