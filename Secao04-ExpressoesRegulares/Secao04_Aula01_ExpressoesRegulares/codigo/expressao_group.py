import re

texto = (r"Meu principal e-mail é evaldowolkers@gmail.com, mas "
         "tenho também o evaldorw@hotmail.com, e o que dizer do "
         "evaldo.wolkers@algumacoisa.com.br? Este eu ainda não "
         "tenho. Que tal também o evaldo-wolkers@algo.com.br?")

padrao = re.compile(r'([\w.-]+)@([\w.-]+)')
resultado = re.search(padrao, texto)

print("resultado.group():", resultado.group())
print("resultado.group(1):", resultado.group(1))
print("resultado.group(2):", resultado.group(2))

resultado = re.findall(r'([\w.-]+)@([\w.-]+)', texto)
print(resultado)

for email in resultado:
    print(email)