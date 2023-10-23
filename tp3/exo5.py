# Nous aurons souvent besoin d’afficher des variables de type Date, donc le plus simple est de créer dès maintenant une procédure dans la classe Date qui affiche cette dernière.
# Si la date reçue en paramètre était le 10 janvier 2025, alors voici l’affichage que vous devez avoir :
# 10/1/2025

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    

print(Date(10, 1, 2025))