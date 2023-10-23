# En utilisant une expression régulière, récupérez les liens du code source et affichez-les.
# Indice: les liens sont contenus dans les attributs href des balises <html> 
import re

with open('index.html', 'r', encoding='utf8') as file:
    content = file.read()
print(content)

regex = r'href="(.+?)"'
matches = re.findall(regex, file.read())
print(matches)
