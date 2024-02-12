import code_de_cesar as cesar
import code_de_vigenere as vigenere
import carre_de_polybe as polybe
import PySimpleGUI as gui

methode = int(input(
    "Choisissez une méthode de chiffrement: 1 -> ROT13 ; 2 -> code de César ; 3 -> code de Vigenère ; 4 -> carre de "
    "Polybe"))
action = int(input("Voulez vous crypter ou décrypter votre message ? 1 -> crypter ; 2 -> décrypter"))
message = input("Entrez le message que vous voulez traiter.")

# ROT13
if methode == 1:
    if action == 1:
        cesar.cryptage_cesar(message, 13)
    elif action == 2:
        cesar.decryptage_cesar(message, 13)
# code de César
elif methode == 2:
    decalage = int(input("Quel décalage voulez-vous appliquer à votre message?"))
    if action == 1:
        cesar.cryptage_cesar(message, decalage)
    elif action == 2:
        cesar.decryptage_cesar(message, decalage)
# code de Vigenère
elif methode == 3:
    cle_vigenere = input("Entrez votre clé de cryptage")
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

# différentes propositions possibles
methode1 = gui.Check("ROT13")
methode2 = gui.Check("César")
methode3 = gui.Check("Vigenère")
methode4 = gui.Check("Polybe")

action1 = gui.Check("crypter")
action2 = gui.Check("décrypter")

message1 = gui.Text("message")
message2 = gui.InputText()

decalage1 = gui.Text("décalage")
decalage2 = gui.InputText()

cle1 = gui.Text("clé")
cle2 = gui.InputText()

boutton1 = gui.Button("OK")
boutton2 = gui.Button("Cancel")

# index des actions
methode = [methode1, methode2, methode3, methode4]
action = [action1, action2]
message = [message1, message2]
decalage = [decalage1, decalage2]
cle = [cle1, cle2]
boutton = [boutton1, boutton2]

# déroulement des étapes
deroulement = [methode, action, message, decalage, cle]

# définition de la fenêtre
etape = 0
contenu = [deroulement[etape], boutton]
window = gui.Window("fenêtre", contenu)

# boucle
while True:
    event, values = window.read()
    # fermeture
    if event == gui.WIN_CLOSED or (event == "Cancel" and etape == 0):
        break
    # retour
    if event == "Cancel":
        etape -= 1
    # suivant
    if event == "OK":
        etape += 1
        contenu = [deroulement[etape], boutton]
        window.Layout(contenu)

window.close()
