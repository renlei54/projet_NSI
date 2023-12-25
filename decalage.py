# import des bibliothèques
import constante as c


def cryptage_decalage(message: str, valeur: int) -> None:
    # initialisation des variables
    sortie = ""
    majuscules: list = []
    # pour chaque caractère de l'entrée
    for lettre in message:
        # si le caractère est une majuscule
        if lettre.isupper():
            lettre = lettre.lower()
            majuscules.append(lettre)
        # si le caractère est dans l'alphabet
        if lettre in c.alphabet:
            # si le caractère était une majuscule
            if lettre in majuscules:
                sortie += str(c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]).upper()
            # si le caractère était une minuscule
            else:
                sortie += c.alphabet[((c.alphabet.index(lettre)) + valeur) % 26]
    print(sortie)


def decryptage_decalage(message: str, valeur: int):
    cryptage_decalage(message, -valeur)
