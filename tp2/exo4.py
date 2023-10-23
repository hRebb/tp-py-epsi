# Soit le dictionnaire suivant, dont les clés sont les noms des élèves et les valeurs sont les listes des notes : d = { "Adam": [12, 15 , 17], "Karim" : [15, 12 , 16], "Joshua": [13, 15 , 7] }
# Ecrire un programme qui remplace les listes des notes par leurs moyennes.

def student_list():
    # Define the dictionary
    med = {
        "Adam": [12, 15, 17],
        "Karim": [15, 12, 16],
        "Joshua": [13, 15, 7]
    }

    result = {}
    for student, grades in med.items():
        average = sum(grades) / len(grades)
        result[student.lower()] = round(average, 2)

    return result

print(student_list())