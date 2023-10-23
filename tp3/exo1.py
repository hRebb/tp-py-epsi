# Ecrire la fonction nb_chiffres_du_carre(n), qui calcule et affiche le nombre de chiffres que comporte l'écriture du carré du nombre n.
# Exemple : Le nombre 8 au carré vaut 64 et 64 est composé de 2 chiffres.
# Indice : La longueur d’une chaine de caractère peut être obtenue grâce à la fonction len().

def nb_chiffres_du_carre(n):
    return len(str(n ** 2))

print(nb_chiffres_du_carre(100))
