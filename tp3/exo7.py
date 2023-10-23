# Maintenant que nous avons notre type Date de créé et quelques procédures et fonctions
# nous permettant de manipuler des variables Date, nous allons pouvoir l’utiliser dans un
# autre type.
# Nous voulons créer un type de donnée permettant de gérer les employés d’une entreprise
# pour un logiciel de gestion.
# Nous allons donc créer un nouveau type de donnée Personne. Chaque Personne aura :
#  Un nom
#  Un prénom
#  Une date de naissance
#  Une date d’embauche

# Coder la classe correspondante pour créer ce nouveau type de donnée.
# Comme vous l’avez fait pour les dates :
# 1. créez une procédure permettant d’afficher en console les informations sur une
# Personne reçue en paramètre.
# 2. créez une fonction permettant de créer une personne par saisie des informations sur
# son nom, prénom, date naissance et date d’embauche.

from exo6 import DateImplementation

class Person():
    def __init__(self, first_name, last_name, birth_date, hire_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def __str__(self):
         return f"{self.first_name} {self.last_name} {self.birth_date} {self.hire_date}"
    
    # @staticmethod
    # def create_person():
    #     first_name = input("Entrez le prénom : ")
    #     last_name = input("Entrez le nom : ")
    #     birth_date = DateImplementation.create_date()
    #     hire_date = DateImplementation.create_date()
    #     return Person(first_name, last_name, birth_date, hire_date)
    
#print(Person("John", "Doe", "07/03/1999", "15/04/2023"))
# print(Person.create_person())