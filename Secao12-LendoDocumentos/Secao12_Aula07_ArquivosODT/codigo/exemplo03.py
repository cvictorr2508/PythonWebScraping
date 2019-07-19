from odf.opendocument import load
from odf import text


doc = load("Copia.odt")
# Percorrendo os parágrafos e imprimindo seu conteúdo
for paragraph in doc.getElementsByType(text.P):
    print(paragraph)