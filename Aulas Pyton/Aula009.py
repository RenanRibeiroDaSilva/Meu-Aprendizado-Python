"""Manipular cadeias de texto"""
frase = 'Curso em Vídeo Python'
print(frase[::2])
"""Cadeia de texto
Na nossa linguagem conhecemos como Frase, em Python string(str)
FATIAMENTO:    [n:n], [:], [n, n, n], [::n]
ANALIZE: frase.len ===> comprimento da frase
         frase.count ===> conta quantos slosts tem a frase
         frase.find ===> encontra uma posição dentro da frase
TRANSFORMAÇÂO: 
         frase.replace ===> reposiciona, troca ou substitui uma palavra na frase
         frase.upper ===> coloca todas a string em maiúsculo
         frase.lower ===> --------#-------#---- em minusculo
         frase.capitalize ===> só o primeiro caractere fica maiúsculo
         frase.title ===> deixa em letra maiúscula todas as letras seguidas de espaço
         frase.strip ===> remove todos os espaços inuteis
         frase.rstrip ===> -------#-----#-----#-- inuteis a direita
         frase.lstrip ===> -------#-----#-----#-- inuteis a esquerda
DIVISÂO:
         frase.split ===> divide as palavras
JUNÇÂO:
         frase.join ===> juntas as palavras
         '-'.frase.join"""
