def leia_dinheiro(txt):
    """
    -> Valida um valos dado pelo usuário
    :param txt: texto digitado pelo usuário
    :return: texto formatado para ser usado como valor
    """
    valido = False
    while not valido:
        entrada = str(input(txt)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
