"""             Ex - 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
                            de Futebol, na ordem de colocação. Depois mostre:
                            a) Os 5 primeiros times.
                            b) Os últimos 4 colocados.
                            c) Times em ordem alfabética.
                            d) Em que posição está o time da Chapecoense."""

#               Como eu fiz

# Tupla:
times = ('Corinthians', 'São Paulo', 'Palmeiras', 'Santos',
         'Cruzeiro', 'Gremio', 'Internacional', 'Atlético Mineiro',
         'Flamengo', 'Fluminense', 'Bota Fogo', 'Chapecoence',
         'Atlético Paranense', 'Avai', 'Ponte Preta', 'Ituano',
         'Bahia', 'Sport', 'Vitória', 'Portuguesa')

print(f'Os cinco primeiros são {times[:5]}')
print(f'Os quatro ultimos são {times[-4:]}')
print(f'Os times em ordem alfabética {sorted(times)}')
for pos, time in enumerate(times):
    if time == 'Chapecoence':
        print(f'E o {time} está ná {pos + 1}° posição na tabela!')
print('Fim')
