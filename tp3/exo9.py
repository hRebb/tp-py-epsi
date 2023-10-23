# Créer une procédure permettant de comparer l’ancienneté de deux employés
# en se basant sur leur date d’embauche. Cette procédure affiche une synthèse de la
# comparaison en console. Exemple :

# Personne : Karim Benzema
# Date de naissance :
# 19/12/1987
# Date d'embauche :
# 18/11/2020

# n'a pas plus d'expérience que :

# Personne : Youcef Belaili
# Date de naissance :
# 14/03/1992
# Date d'embauche :
# 26/10/2017

from exo7 import Person

class PersonCompare(Person):
    def __init__(self, first_name, last_name, birth_date, hire_date):
        super().__init__(first_name, last_name, birth_date, hire_date)
    
    @staticmethod
    def compare_employees(employee1, employee2):
        hire_date1 = tuple(map(int, employee1.hire_date.split("/")))
        hire_date2 = tuple(map(int, employee2.hire_date.split("/")))
        
        if hire_date1 > hire_date2:
            older_employee, younger_employee = employee1, employee2
        elif hire_date1 < hire_date2:
            older_employee, younger_employee = employee2, employee1
        else:
            print(f"{employee1.first_name} {employee1.last_name} et {employee2.first_name} {employee2.last_name} ont été embauchés en même temps")
            return
        
        print(f"{older_employee.first_name} {older_employee.last_name} est plus ancien que {younger_employee.first_name} {younger_employee.last_name}")

employee1 = Person("Karim", "Benzema", "19/12/1987", "18/11/2020")
employee2 = Person("Youcef", "Belaili", "14/03/1992", "26/10/2017")

PersonCompare.compare_employees(employee1, employee2)