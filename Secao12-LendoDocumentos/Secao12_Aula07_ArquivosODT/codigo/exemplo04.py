import ezodf

# Abrindo um documento
doc = ezodf.opendoc('copia.odt')
# Salvando um documento utilizando "Salvar como"
doc.saveas("copia2.odt")