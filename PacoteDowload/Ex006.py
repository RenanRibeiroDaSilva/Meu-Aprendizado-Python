"""Ex 006 - Crie um algoritmo que leio um número e mostre o seu dobro, triplo e sua raiz
quadrada."""

#Recebendo dados
n1 = int(input('Digite um valor:'))
dbr = n1 * 2
tpl = n1 * 3
rzq = n1 ** (1/2)#Também posso faze uso do pow(n (1,2)

#Processando e imprimindo dados para o usuário
print('Analisando o valor {}, descobrimos que:'.format(n1))
print('O seu dobro é: {}'.format(dbr))
print('O seu triplo é: {}'.format(tpl))
print('E sua Raiz Quadrada é: {:.2f}'.format(rzq))
