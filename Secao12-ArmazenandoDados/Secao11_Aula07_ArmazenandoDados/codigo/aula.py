from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import mysql.connector
import re

dados_conexao = {"user":"root","password":"1234","host":'127.0.0.1',"database":"scraping","charset":"utf8"}

conexao = mysql.connector.connect(**dados_conexao)
cursor = conexao.cursor()

def gravar(titulo, url, conteudo):
    cursor.execute("insert into paginas (titulo, url, conteudo) values (%s,%s,%s)", (titulo, url, conteudo))
    conexao.commit()

def getLinks(urlArtigo):
    url = 'http://pt.wikipedia.org' + urlArtigo
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    titulo = bs.find('h1').get_text()
    conteudo = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    gravar(titulo, url, conteudo)
    return bs.find('div', {'id':'bodyContent'}).\
        findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Copa_do_Mundo_FIFA_de_2026')

try:
    contador = 1
    while len(links) > 0 and contador <= 10:
        novoArtigo = links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks(novoArtigo)
        contador += 1
finally:
    cursor.close()
    conexao.close()