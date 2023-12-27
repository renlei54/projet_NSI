# import des bibliothèques
import constante as c


def cryptage_decalage(entree: str, valeur: int) -> None:
    # initialisation des variables
    sortie = ""
    majuscules: list = []
    caracteres_speciaux: list = []
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
    print(sortie)



def decryptage_decalage(entree: str, valeur: int):
    cryptage_decalage(entree, -valeur)
