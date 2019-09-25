# Simulando o login_cookie.html
import requests


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " \
             "AppleWebKit/537.36 (KHTML, like Gecko)" \
             "Chrome/35.0.1916.47 Safari/537.36"

params = {'login':'evaldo','senha':'1234'}
#r = requests.post("http://localhost:8000/login_cookie.php", data=params)
r = requests.post("http://www.pythonparatodos.com.br/secao14aula02cookie/"
                  "login_cookie_sem_redirect.php", headers={'User-Agent': user_agent}, data=params)
print("Cookies:", r.cookies.get_dict())
#r = requests.post("http://localhost:8000/principal_cookie.php", cookies=r.cookies)
r = requests.post("http://www.pythonparatodos.com.br/secao14aula02cookie/"
                  "principal_cookie.php", headers={'User-Agent': user_agent}, cookies=r.cookies)
print(r.text)