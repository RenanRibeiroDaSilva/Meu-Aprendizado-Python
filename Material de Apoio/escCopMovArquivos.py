import shutil
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_nota)})
    return lista_media


def copia_arquiva(nome_arquivo):
    shutil.copy(nome_arquivo, "C:/Users/renan/Desktop/notas_alunos.txt")


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, "C:/Users/renan/Desktop/teste/notas_alunos.txt")


if __name__ == '__main__':
    move_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Nathalia, 10, 10, 10, 9\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
