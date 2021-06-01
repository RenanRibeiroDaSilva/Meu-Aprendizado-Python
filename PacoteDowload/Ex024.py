"""     Ex - 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo". """

# Criamos uma variavel cid para atribuirmos o valor digitado pelo usuario
cid = str(input('Em que cidade você nasceu? ')).strip() # Usamos o strip() para excluir os espaços vazios e
print(cid[0:5].upper() == 'SANTO')                      # depois da string.
            # Usamos o upper() para colocar toda a string e maiúsculo e assim reconhecer todos os resultados
            # com letras maiúsculas, independente da forma como o usuario venha digitar o nome da cidade. Levando
            # em consideração apenas se o resultato é o mesmo que desejamos obter ou não.