import ezodf

documento = ezodf.opendoc('arquivonovo.odt')
# Pegando o primeiro objeto do texto
p1 = documento.body[0]
print(p1)
print(p1.text)
# Quantidade de objetos do documento
count = len(documento.body)
print(count)