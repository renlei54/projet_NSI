# import des modules
import constante as c


# fonction de cryptage
def cryptage_polybe(entree: str) -> None:
    # initialisation des variables
    sortie: str = ""
    majuscules: list = []
    caracteres_speciaux: list = []
    # pour chaque caractère de l'entrée
    for lettre in entree:
        # si le caractère est un w
        if lettre == "W" or lettre == "w":
            lettre.lower()
            # ajout de 2 v
            sortie += str(c.polybe.index("v") // 5 + 1)
            sortie += str(c.polybe.index("v") % 5 + 1)
            sortie += str(c.polybe.index("v") // 5 + 1)
            sortie += str(c.polybe.index("v") % 5 + 1)
        # si le caractère est une lettre
        elif lettre in c.polybe or lettre.isupper():
            lettre = lettre.lower()
            sortie += str(c.polybe.index(lettre) // 5 + 1)
            sortie += str(c.polybe.index(lettre) % 5 + 1)
        # si le caractère est un caractère spécial
        else:
            sortie += lettre
    print(sortie)


# fonction de décryptage
def decryptage_polybe(entree: str) -> None:
    # initialisation des variables
    sortie: str = ""
    sortie_finale: str = ""
    # dédoublement des caractères qui ne sont pas des chiffres
    for lettre in entree:
        if lettre.isdigit():
            sortie += lettre
        else:
            # dédoublement du caractère
            sortie += lettre
            sortie += lettre
    # décryptage du message
    for i in range(0, len(sortie), 2):
        # décryptage des lettres
        if sortie[i].isdigit():
            sortie_finale += c.polybe[(int(sortie[i])-1) * 5 + int(sortie[i+1]) - 1]
        # ajout des caractères spéciaux
        else:
            sortie_finale += sortie[i]
    print(sortie_finale)

