"""         Ex - 095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
                        de visualização de detalhes do aproveitamento de cada jogador."""

#           Como eu fiz.

# T.L.D.:
cad_joga = dict()
gol_part = list()
dad_jgdr = list()

# Area de desenvolvimeno:
while True:

    # Código de cadastro dos jogadores:
    cad_joga.clear()
    gol_part.clear()
    cad_joga['nome'] = str(input('Nome do jogador: ')).strip().title()
    tot_part = int(input(f'Quantas partidas {cad_joga["nome"]} jogou: '))
    for j in range(0, tot_part):
        gol_part.append(int(input(f'Quantos gols na {j + 1}º partida: ')))
    cad_joga['gols'] = gol_part[:]
    tot_gols = sum(gol_part)
    cad_joga['totGols'] = tot_gols
    dad_jgdr.append(cad_joga.copy())

    # Perguntar se o usuario deseja continuar o cadastro de jogadores:
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor selecione uma das opçõe [S/N]: ')
    if resp in 'N':
        break
# Imprimir os dados para o usuário:
print(f'{"":-^60}')
print(f'{">JOGADORES CADASTRADOS<":^60}')
print(f'{"Código":-<10}{"Nome do Jogador":-<30}{"Total de Gols":->20}')
for i, n in enumerate(dad_jgdr):
    print(f'{i+1:.<10}{n["nome"]:.<30}{n["totGols"]:.>20}')
print(f'{"":-^60}')
# Perguntar qual jogador o usuário deseja visializar as partidas detalhadas:
while True:
    codigo = int(input('''Digite o código do jogador que quer visualizar 
detalhadamente os gols por partida [999 para finaliza]: '''))
    for i, n in enumerate(dad_jgdr):
        if codigo == i + 1:
            print(f'{">PARTIDA DETALHADA<":^60}')
            print(f'jogador: {n["nome"]}')
            print(f'{"Partida:":-<30}{"Gols:":->30}')
            for c, v in enumerate(dad_jgdr[i]['gols']):
                print(f'{c + 1}º partida:{v:.>49}')
                print(f'{"":=^60}')
        else:
            print(f'{"":=^60}')
            print(f'Não existe jogador com o código {codigo}!')
            print(f'{"":=^60}')
    if codigo == 999:
        break
print(f'{"FINALIZANDO O PROGRAMA!":~^60}')
print(f'{"VOlte sempre!":_^60}')
print(f'FIM...')
