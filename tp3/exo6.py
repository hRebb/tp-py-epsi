# Nous aurons aussi besoin à de nombreuses reprises de créer des variables de type Date
# et de les remplir avec des valeurs saisies par l’utilisateur.
# Or ces saisies doivent être systématiquement vérifiées pour éviter que les utilisateurs
# n’entrent des valeurs incohérentes ou des dates impossibles. Pour ne pas avoir à coder
# plusieurs fois cette demande de saisie et ces vérifications vous allez créer une fonction qui ne reçoit aucun paramètre et qui retourne un objet Date correctement remplit par
# l’utilisateur.
# La fonction créera l’objet vide, demandera à l’utilisateur l’année, puis le mois et enfin le
# jour de la date à créer. Chaque saisie sera vérifiée puis, si elle est correcte, sera
# enregistrée dans la variable de type Date. Lorsque les 3 composantes de la date (année,
# mois, jour) seront enregistrés, la variable sera retournée par la fonction.
# Vous choisirez un nom approprié pour cette fonction.
# Voici un exemple d’exécution :
# Entrez l’année : 2025
# Entrée le mois : 01
# Entrez le jour : 10
# 10/01/2025
# Cette fonction aura la responsabilité de vérifier chacune des données saisies pour ne pas
# que l’utilisateur puisse entrer de Date invalide.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class DateImplementation(Date):
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    @staticmethod
    def create_date():
        day = int(input("Entrez le jour : "))
        month = int(input("Entrez le mois : "))
        year = int(input("Entrez l'année : "))
        return DateImplementation(day, month, year)
    
print(DateImplementation.create_date())