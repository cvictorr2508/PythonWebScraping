from odf.opendocument import load
from odf import text

# Abrindo um documento
doc = load("Copia.odt")
# Obtendo todo conteúdo do documento
conteudo = doc.text
print(conteudo)
