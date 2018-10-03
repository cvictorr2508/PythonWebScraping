from urllib.request import urlopen
paginaTexto = urlopen("http://bgcrm.ru/changes.txt")
print(str(paginaTexto.read(), "utf-8"))