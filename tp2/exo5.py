# Écrire un programme qui demande à l’utilisateur de saisir un chiffre N, puis qui calcule et affiche le résultat de factorielle de N.
# Rappel Factorielle de N : Fact(N) = 1 x 2 x ... x N

def n_factorial():
    num = int(input("Enter a number: "))
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(n_factorial())