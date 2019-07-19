import ezodf


documento = ezodf.opendoc('arquivonovo.odt')
# Criando uma lista
lista = ezodf.ezlist(['Laranja', 'Maçã', 'Banana'])
documento.body.append(lista)
documento.save()