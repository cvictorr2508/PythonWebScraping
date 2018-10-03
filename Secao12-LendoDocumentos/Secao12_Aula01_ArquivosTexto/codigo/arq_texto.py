from urllib.request import urlopen
paginaTexto = urlopen("http://mezuro.org/humans.txt")
print(paginaTexto.read())