# Instanciez le dictionnaire suivant : etudiants = { "etudiant_1":13, "etudiant_2":17, "etudiant_3":9, "etudiant_4":15, "etudiant_5":8, "etudiant_6":14, "etudiant_7":14, "etudiant_8":12, "etudiant_9":13, "etudiant_10":15, "etudiant_11":14, "etudiant_112":9, "etudiant_13":12, "etudiant_14":12, "etudiant_15":13, "etudiant_16":7, "etudiant_17":12, "etudiant_18":15, "etudiant_19":9, "etudiant_20":17 }
# Ecrire un programme Python qui ajoute l’étudiant 21 (ayant eu 18), et partitionne ce dictionnaire en deux sous dictionnaires : etudiantAdmis (note >= 10) et etudiantNonAdmis (note < 10)

def partition_students(etudiants):
    # Add the student 21
    etudiants["etudiant_21"] = 18

    # Partition the dictionary
    etudiantAdmis = {}
    etudiantNonAdmis = {}

    for key, value in etudiants.items():
        if value >= 10:
            etudiantAdmis[key] = value
        else:
            etudiantNonAdmis[key] = value

    print(f"Admis : {etudiantAdmis}, Non admis : {etudiantNonAdmis}")

print(partition_students(etudiants = {
        "etudiant_1":13,
        "etudiant_2":17,
        "etudiant_3":9,
        "etudiant_4":15,
        "etudiant_5":8,
        "etudiant_6":14,
        "etudiant_7":14,
        "etudiant_8":12,
        "etudiant_9":13,
        "etudiant_10":15,
        "etudiant_11":14,
        "etudiant_112":9,
        "etudiant_13":12,
        "etudiant_14":12,
        "etudiant_15":13,
        "etudiant_16":7,
        "etudiant_17":12,
        "etudiant_18":15,
        "etudiant_19":9,
        "etudiant_20":17
    }))