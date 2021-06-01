"""     Ex - 025 - Crie um programa que leie o nome de uma pessoa e diga se ela tem "Silva" no nome."""


# Criamos a var nome para atribuirmos o valor digitado pelo usuario.
nome = str(input('Qual seu nome completo?')).strip() # Usamos strip() para não aceitarmos espaços vazios antes e depois
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # da string.
                                        # Usamos o operador IN para verificar se dentro da string a um resultado
                                        # igual ao que desejamos encotrar. E para diminuir erros colocamos o nosso
                                        # resultado em minúsculo e usamos o lower() para colocar toda a string em
                                        # letras minúsculas.