# Simulando o login_session.html
import requests

session = requests.Session()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " \
             "AppleWebKit/537.36 (KHTML, like Gecko)" \
             "Chrome/35.0.1916.47 Safari/537.36"

params = {'login':'evaldo','senha':'1234'}
r = requests.post("http://localhost:8000/login_session.php", data=params)
#r = session.post("http://www.pythonparatodos.com.br/secao14aula03session/"
#                  "login_session.php", headers={'User-Agent': user_agent}, data=params)
print(r.text)