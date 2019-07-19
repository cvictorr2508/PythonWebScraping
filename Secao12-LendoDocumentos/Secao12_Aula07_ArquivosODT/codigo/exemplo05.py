import ezodf

doc = ezodf.opendoc('copia.odt')

# Imprimindo propriedades do documento
titulo = doc.meta['title']
print(titulo)
data = doc.meta['date']
print(data)
generator = doc.meta['generator']
print(generator)
description = doc.meta['description']
print(description)
paginas = doc.meta.count['page']
print(paginas)