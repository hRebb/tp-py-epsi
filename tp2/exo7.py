# Ecrire un programme qui permet d'afficher à l'écran une table de multiplication de dimension n, ayant la forme donnée par l’exemple suivant.
# Par exemple si n==4 :
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(i * j, end=" ")
        print()

print(multiplication_table())