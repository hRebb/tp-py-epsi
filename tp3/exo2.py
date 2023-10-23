# Ecrire une fonction estPremier() qui reçoit en paramètre un nombre et retourne true s'il s'agit d'un nombre premier, false sinon.
# indice : modulo (%)

def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(est_premier(7))
print(est_premier(8))