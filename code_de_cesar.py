# import des bibliothèques
import constante as c


def cryptage_cesar(entree: str, valeur: int) -> str:
    # initialisation des variables
    sortie = ""
    # pour chaque caractère de l'entrée
    for lettre in entree:
        # si le caractère est une minuscule
        if lettre in c.alphabet:
            sortie += c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]
        # si le caractère est une majuscule
        elif lettre.isupper():
            lettre = lettre.lower()
            sortie += str(c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]).upper()
        # si le caractère est un caractère spécial
        else:
            sortie += lettre
    return sortie


# fonction de décryptage
def decryptage_cesar(entree: str, valeur: int) -> str:
    return cryptage_cesar(entree, -valeur)
