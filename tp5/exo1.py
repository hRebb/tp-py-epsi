# Récupérer le code source de la page web dans le fichier index.html, et affichez le dans une console.
with open('index.html', 'r', encoding='utf8') as file:
    print(file.read())