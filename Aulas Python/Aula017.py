"""         Aula - 017 - Listas!
            Variáveis Compostas (Listas)"""

# Teoria:
'''As listas permitem as modificações das variáveis que estão dentro delas
para criar uma lista usamos [](colcehtes) ao invés dos parenteses que usamos para criar
as tuplas.

# Adicionar elementos:
lista.append('item') --------------> Adiciona item no final da lista.
lista.insert(0, 'novo item) -------> Adiciona novo item na posição que indicamos.

# Deletar elementos:
del lista[3] ----------------------> Deleta a posição indicada na lista. Obs: del é um comando e não um método.
lista.pop(3) ----------------------> Deleta a posição indicada na lista. Obs: pop é um metodo.
lista.remove('item') --------------> Deleta o valor indicado na lista.
Obs: Os comandos ou métodos que eliminam os  itens por seu valor ou por sua indexação, depos reposicinam os 
valores a frente caso não seja o ultimo index.

# Organiza a lista:
lista.sort() ----------------------> Organiza a lista em ordem crescente.
lista.sort(reverse=Trues) ---------> Organiza a lista em ordem decresente.
len(valores) ----------------------> Devolve o tamanho da lista.
'''

# Prática:

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegeui ao final da lista')


a = [2, 3, 4, 7]
b = a  # Aqui fizemos uma ligação de lista e não uma cópia. Sempre que alterarmos o valor de um também será alterado o
b[2] = 8  # valor do outro.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]  # Aqui fizemos uma cópia de lista e não uma ligação. Agora quando alterarmos o valor de uma lista a outra não
b[2] = 8  # será alterada.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
