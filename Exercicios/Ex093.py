"""         Ex - 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
                        o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
                        em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de
                        gols feitos durante o campeonato."""

#               Como eu fiz.

# T.L.D.:
jogad = dict()
gols = list()
soma = 0
jogad['nome'] = str(input('Nome do jogador: ')).strip().title()
qtd_p = int(input(f'Quantas partida {jogad["nome"]} jogou: '))

# Laço de repetição:
for j in range(0, qtd_p):
    gols.append(int(input(f'Quanto gols no {j + 1}º jogo: ')))
jogad['gols'] = gols[:]
for g in jogad['gols']:
    soma += g
jogad['total_gols'] = soma
print(f'{"":=^60}')
print(f'{jogad}')
print(f'{"":=^60}')
for k, v in jogad.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{"":=^60}')
print(f'O jogador {jogad["nome"]} jogou {qtd_p} jogos')
for i, v in enumerate(jogad['gols']):
    print(f'{"=>":>5} Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogad["total_gols"]} gols')

#           Como o Guanabara fez.
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantas gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k}, tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
