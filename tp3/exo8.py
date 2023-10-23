# Créer une fonction permettant de comparer 2 dates :
# estPlusRecenteQue(date1, date2)
# Cette fonction reçoit 2 dates et retourne true si la date1 est plus recente que la date2,
# sinon si la date2 est plus recente ou égale à la date1 alors elle retourne false.

from exo6 import Date

class DateCompare(Date):
    def __init__(self, day, month, year):
        super().__init__(day, month, year)
    
    @staticmethod
    def is_more_recent(date1, date2):
        if date1.year > date2.year:
            return True
        elif date1.year == date2.year:
            if date1.month > date2.month:
                return True
            elif date1.month == date2.month:
                if date1.day > date2.day:
                    return True
        return False
    
# print(DateCompare.is_more_recent(Date(10, 10, 1000), Date(10, 10, 1999)))