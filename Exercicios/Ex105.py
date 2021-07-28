"""         Ex - 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
            retornar um dicionário com as seguintes informações:
            – Quantidade de notas
            – A maior nota
            – A menor nota
            – A média da turma
            – A situação (opcional)
"""

# Como eu fiz.


# Função:
def notasR(nota, ok=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota: uma lista de notas
    :param ok: valor opcional, indicando deve ou não adicionar a situação.
    :return: dicionário com várias informações da turma.
    """
    notas = {}
    cont = maior = menor = soma = media = 0
    for n in range(0, len(nota)):
        cont += 1
    notas['qtdNotas'] = cont
    for m in nota:
        if m == 0 or maior < m:
            maior = m
    notas['maiNota'] = maior
    cont = 0
    for m in nota:
        cont += 1
        if cont == 1 or menor > m:
            menor = m
    notas['menNota'] = menor
    for m in nota:
        soma += m
    notas['medNota'] = soma / len(nota)
    media = soma / len(nota)
    if ok:
        if media >= 7:
            notas['situação'] = 'APROVADO'
        elif media >= 5:
            notas['situação'] = 'de RECUPERAÇÃO'
        elif media <= 4:
            notas['situação'] = 'REPROVADO'
    return notas


# Programa principal:
notLis = []
mosLis = []

while True:
    print('-=' * 50)
    n = float(input('Qual a nota do aluno: '))
    notLis.append(n)
    while True:
        res = str(input('Quer adicionar mais uma nota? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[0;31mErro! Resposta inválida\033[m')
    if res in 'N':
        break

while True:
    print('-=' * 50)
    res = str(input('Quer ver a situação do aluno? [S/N] ')).strip().upper()[0]
    if res in 'SN':
        break
    print('\033[0;31mErro! Resposta inválida\033[m')
if res in 'S':
    mosLis.append(notasR(notLis, ok=True))
else:
    mosLis.append(notasR(notLis))
print('-=' * 50)
print(f'Foram adicionadas {mosLis[0]["qtdNotas"]} notas.')
print(f'A maior nota do aluno foi {mosLis[0]["maiNota"]}.')
print(f'A menor nota do aluno foi {mosLis[0]["menNota"]}.')
print(f'A media foi {mosLis[0]["medNota"]:.1f}.')
if res in 'S':
    print(f'E o aluno está {mosLis[0]["situação"]}.')
print('-=' * 50)

# Como o Guanabara fez.


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando deve ou não adicionar a situação.
    :return: dicionário com várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas())
