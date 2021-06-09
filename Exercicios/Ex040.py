"""         Ex - 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
                        no final, de acordo com a média atingida:
                        - Média abaixo de 5.0:
                        REPROVADO
                        - Média entre 5.0 e 6.9:
                        RECUPERAÇÃO
                        - Média 7.0 ou superior:
                        APROVADO """

#               Como eu Fiz

# Criar variaveis e receber dados do usuario
nota_1 = float(input('Qual a primeira nota do aluno? '))
nota_2 = float(input('Qual a segunda nota do aluno? '))

# Fazer os calculos matemático
media = (nota_1 + nota_2) / 2

# Criar as condições para mostrar o resultado ao usuário
if media <= 5.0:
    print('Sua média foi \033[31m{:.1f}\033[m e infelizmente você está\033[31m REPROVADO\033[m!'.format(media))
elif 5.1 <= media <= 6.9:
    print('Sua média foi \033[33m{:.1f}\033[m e você está de\033[33m RECUPERAÇÃO\033[m!'.format(media))
elif media >= 7.0:
    print('Parabéns!!! Sua média foi \033[32m{:.1f}\033[m e você está\033[32m APROVADO\033[m!'.format(media))
print('-Fim-')

#       Como o Professor Guanabara Fez
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota.: '))
média = (nota_1 + nota_2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota_1, nota_2, média))
if 7 >  média >= 5:
    print(' O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média > 7:
    print('O aluno está APROVADO')
