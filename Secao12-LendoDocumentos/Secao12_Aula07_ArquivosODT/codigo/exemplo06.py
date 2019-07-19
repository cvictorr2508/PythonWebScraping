import ezodf
from ezodf import Paragraph

# Criando um documento novo
documento = ezodf.newdoc(doctype="odt", filename="arquivonovo.odt", template=None)
# Adicionando um parágrafo e armazenando o objeto na variável p1
p1 = documento.body.append(Paragraph('Meu terceiro parágrafo.'))
# Adicionando um parágrafo antes do parágrafo p1
documento.body.insert_before(p1, Paragraph('Meu segundo parágrafo.'))
# inserindo um parágrafo passando o índice 0, ele vai ser inserido no
# início do documento
documento.body.insert(0, Paragraph('Meu primeiro parágrafo.'))

# Salvando o documento
documento.save()