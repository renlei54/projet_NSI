import code_de_cesar as cesar
import code_de_vigenere as vigenere
import carre_de_polybe as polybe

methode: int = int(input("Choisissez une méthode de chiffrement: 1 -> ROT13 ; 2 -> code de César ; 3 -> code de Vigenère ; 4 -> carre de Polybe"))
action: int = int(input("Voulez vous crypter ou décrypter votre message ? 1 -> crypter ; 2 -> décrypter"))
message: str = input("Entrez le message que vous voulez traiter.")

# ROT13
if methode == 1:
    if action == 1:
        cesar.cryptage_cesar(message, 13)
    elif action == 2:
        cesar.decryptage_cesar(message, 13)
# code de César
elif methode == 2:
    decalage: int = int(input("Quel décalage voulez-vous appliquer à votre message?"))
    if action == 1:
        cesar.cryptage_cesar(message, decalage)
    elif action == 2:
        cesar.decryptage_cesar(message, decalage)
# code de Vigenère
elif methode == 3:
    cle_vigenere: str = input("Entrez votre clé de cryptage")
    if action == 1:
        vigenere.cryptage_vigenere(message, cle_vigenere)
    elif action == 2:
        vigenere.decryptage_vigenere(message, cle_vigenere)
# carré de Polybe
elif methode == 4:
    if action == 1:
        polybe.cryptage_polybe(message)
    elif action == 2:
        polybe.decryptage_polybe(message)
        polybe.decryptage_polybe(message)

