# Écrire un programme qui calcule et retourne la moyenne de N notes.
# Le programme demande préalablement de saisir le nombre de notes à comptabiliser, puis l’utilisateur saisit les N notes.

def average():
    num = int(input("Enter the number of notes: "))
    result = 0
    for i in range(1, num + 1):
        result += int(input(f"Enter the note {i}: "))
    result / num
    return round(result / num)

print(average())