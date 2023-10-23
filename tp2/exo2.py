# Instanciez le dictionnaire suivant :
# maroc = {"president": "Mohamed VI", "capitale": "Rabat", "superficie": 710850}
# algerie = {"president": "Abdelaziz Bouteflika", "capitale": "Alger", "superficie": 2382000}
# tunisie = {"president": "Kaïs Saïed", "capitale": "Tunis", "superficie": 163610}

# Mettez à jour le nom du président Algérien (par la valeur « Abdelmadjid Tebboune ») puis intégrez ces 3 dictionnaires dans 1 seul.


def combine_countries():
    # Define the dictionaries
    maroc = {"president": "Mohamed VI", "capitale": "Rabat", "superficie": 710850}
    algerie = {"president": "Abdelaziz Bouteflika", "capitale": "Alger", "superficie": 2382000}
    tunisie = {"president": "Kaïs Saïed", "capitale": "Tunis", "superficie": 163610}

    # Update the president of Algeria
    algerie["president"] = "Abdelmadjid Tebboune"

    # Combine the dictionaries    pays = {"maroc": maroc, "algerie": algerie, "tunisie": tunisie}
    pays = {
        "maroc": maroc,
        "algerie": algerie,
        "tunisie": tunisie
    }

    return pays

print(combine_countries())