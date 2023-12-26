# import des bibliothèques
import constante as c


def cryptage_decalage(message: str, valeur: int) -> None:
    # initialisation des variables
    sortie = ""
    majuscules: list = []
    caracteres_speciaux: list = []
    # pour chaque caractère de l'entrée
    for lettre in message:
        # si le caractère est une majuscule
        if lettre.isupper():
            lettre = lettre.lower()
            sortie += str(c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]).upper()
        # si le caractère est un caractère spécial
        elif lettre not in c.alphabet:
            sortie += lettre
        # si le caractère est une minuscule
        elif lettre in c.alphabet:
            sortie += c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]
    print(sortie)


def decryptage_decalage(message: str, valeur: int):
    cryptage_decalage(message, -valeur)
