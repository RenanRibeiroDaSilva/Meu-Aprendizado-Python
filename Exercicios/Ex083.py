"""     Ex - 083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
                    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
                    e fechados na ordem correta."""

#           Como eu fiz.

# Var:
exp = str(input('Digite a expressão: '))
c_abre = c_fecha = 0

for l in exp:
    if l == '(':
        c_abre += 1
    if l == ')':
        c_fecha += 1

if c_abre == c_fecha:
    print(f'Há expressão {exp} é valida!')
else:
    print(f'Há expressão {exp} não é valida!')

#           Como o Guanabara fez
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
