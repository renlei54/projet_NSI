import code_de_cesar as cesar
import code_de_vigenere as vigenere
import carre_de_polybe as polybe
import PySimpleGUI as gui

# methode = int(input(
#     "Choisissez une méthode de chiffrement: 1 -> ROT13 ; 2 -> code de César ; 3 -> code de Vigenère ; 4 -> carre de "
#     "Polybe"))
# action = int(input("Voulez vous crypter ou décrypter votre message ? 1 -> crypter ; 2 -> décrypter"))
# message = input("Entrez le message que vous voulez traiter.")

# # ROT13
# if methode == 1:
#     if action == 1:
#         cesar.cryptage_cesar(message, 13)
#     elif action == 2:
#         cesar.decryptage_cesar(message, 13)
# # code de César
# elif methode == 2:
#     decalage = int(input("Quel décalage voulez-vous appliquer à votre message?"))
#     if action == 1:
#         cesar.cryptage_cesar(message, decalage)
#     elif action == 2:
#         cesar.decryptage_cesar(message, decalage)
# # code de Vigenère
# elif methode == 3:
#     cle_vigenere = input("Entrez votre clé de cryptage")
#     if action == 1:
#         vigenere.cryptage_vigenere(message, cle_vigenere)
#     elif action == 2:
#         vigenere.decryptage_vigenere(message, cle_vigenere)
# # carré de Polybe
# elif methode == 4:
#     if action == 1:
#         polybe.cryptage_polybe(message)
#     elif action == 2:
#         polybe.decryptage_polybe(message)
#         polybe.decryptage_polybe(message)

# GUI : choix méthode de chiffrement
met_rot13 = gui.Radio("ROT13",    "methode",       key="met_rot13", enable_events=True, default=True)
met_cesar = gui.Radio("César",    "methode",       key="met_cesar", enable_events=True)
met_vigen = gui.Radio("Vigenère", "methode",       key="met_vigen", enable_events=True)
met_polyb = gui.Radio("Polybe",   "methode",       key="met_polyb", enable_events=True)

# GUI : action
action_crypter = gui.Radio("crypter",   "action",   key="action_crypter",  enable_events=True, default=True)
action_decrypt = gui.Radio("décrypter", "action",   key="action_decrypt",  enable_events=True)

# GUI : message
msg_label = gui.Text("message",  key="msg_label")
msg_input = gui.InputText(       key="msg_input")

# GUI : décalage
decalage_label = gui.Text("décalage", key="decalage_label", visible=False)
decalage_input = gui.InputText(       key="decalage_input", visible=False)

# GUI : clé
cle_label = gui.Text("clé",  key="cle_label", visible=False)
cle_input = gui.InputText(   key="cle_input", visible=False)

# GUI : résultat
res_label   = gui.Text("résultat",  key="res_label")
res_donnees = gui.Text(key="res_donnees")

# GUI : boutons
bouton_ok     = gui.Button("OK",      key="bouton_ok")
bouton_fermer = gui.Button("Fermer",  key="bouton_fermer")

# Construction de la fenêtre
window  = gui.Window("fenêtre", [
        [met_rot13,      met_cesar,     met_vigen, met_polyb],
        [action_crypter, action_decrypt                     ],
        [msg_label,      msg_input                          ],
        [decalage_label, decalage_input                     ],
        [cle_label,      cle_input                          ],
        [res_label,      res_donnees                        ],
        [bouton_ok,      bouton_fermer                      ]
    ])

# Fonction de visibilité
def visibilite_groupe(prefixe, visibilite):
    for key in window.key_dict.keys():
        if key.startswith(prefixe):
            window[key].update(visible=visibilite)

# Méthode choisie
methode_choisie = "met_rot13"

# Action choisie
action_choisie = "action_crypter"

# GUI : boucle principale
while True:
    event, values = window.read()
    if event:
        # changement méthode
        if event.startswith("met_"):
            methode_choisie = event
            visibilite_groupe("cle",        values["met_vigen"])
            visibilite_groupe("decalage",   values["met_cesar"])
        # changement action
        elif event.startswith("action_"):
            action_choisie = event
            
    # fermeture
    if event == gui.WIN_CLOSED or event == "bouton_fermer":
        break
    if event == "bouton_ok":
        if methode_choisie == "met_rot13":
            res_donnees.update(cesar.cryptage_cesar(values["msg_input"], 13))
        elif methode_choisie == "met_cesar":
            try:
                decalage = int(values["decalage_input"])
            except:
                decalage = 0
            if action_choisie == "action_crypter":
                res_donnees.update(cesar.cryptage_cesar(values["msg_input"], decalage))
            elif action_choisie == "action_decrypt":
                res_donnees.update(cesar.decryptage_cesar(values["msg_input"], decalage))
        elif methode_choisie == "met_vigen":
            if action_choisie == "action_crypter":
                res_donnees.update(vigenere.cryptage_vigenere(values["msg_input"], values["cle_input"]))
            elif action_choisie == "action_decrypt":
                res_donnees.update(vigenere.decryptage_vigenere(values["msg_input"], values["cle_input"]))

        elif methode_choisie == "met_polyb":
            if action_choisie == "action_crypter":
                try:
                    res_donnees.update(polybe.cryptage_polybe(values["msg_input"]))
                except:
                    res_donnees.update("Veuillez entrer un message valide")
            elif action_choisie == "action_decrypt":
                try:
                    res_donnees.update(polybe.decryptage_polybe(values["msg_input"]))
                except:
                    res_donnees.update("Veuillez entrer un message valide")
    
            
        # print(methode_choisie)
        # print(action_choisie)
        # print(msg_input.get())
        # res_donnees.update(values["msg_input"])
        

window.close()
