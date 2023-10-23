# Nous souhaitons créer un nouveau type de donnée : Date
# Une date sera composée de 3 entiers :
#  Le jour
#  Le mois
#  L’année
# Exercice 4
# Créez la classe correspondante.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year