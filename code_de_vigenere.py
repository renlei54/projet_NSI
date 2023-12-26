# import des bibliothèques
import constante as c


# fonction de cryptage
def cryptage_vigenere(entree: str, cle: str):
    sortie = ""
    # retrait des caractères speciaux et des majuscules
    # nouvelle cle avec des minuscules uniquement
    nouvelle_cle = ""
    # remise en minuscule
    cle = cle.lower()
    for lettre in cle:
        # ajout des lettres uniquements
        if lettre in c.alphabet:
            nouvelle_cle += lettre
    # nouvelle entree avec uniquement des minuscules
    nouvelle_entree: str = ""
    majuscules: list = []
    caracteres_speciaux: list = []
    for a in range(len(entree)):
        # si c'est une majuscule
        if entree[a].isupper():
            majuscules.append(a)
            nouvelle_entree += entree[a].lower()
        # si c'est une minuscule
        elif entree[a] in c.alphabet:
            nouvelle_entree += entree[a]
        # si c'est un caractère spécial
        elif entree[a].lower() not in c.alphabet:
            caracteres_speciaux.append(a)
    # mise de l'entree et de la clé à la même taille
    while len(nouvelle_cle) < len(nouvelle_entree):
        nouvelle_cle += nouvelle_cle
    nouvelle_cle = nouvelle_cle[:len(nouvelle_entree)]
    # cryptage
    # pour chaque lettre minuscule de l'entree
    for i in range(len(nouvelle_entree)):
        # calcul des coordonnées dans la table
        y: int = c.alphabet.index(nouvelle_cle[i])
        x: int = c.alphabet.index(nouvelle_entree[i])
        # ajout de la lettre chifrée à la sortie
        sortie += c.table_de_vigenere[y][x]
    # remise en place des majuscules et des caractères speciaux
    sortie_finale: str = ""
    h: int = 0
    for i in range(len(entree)):
        # ajout des caractères spéciaux
        if i in caracteres_speciaux:
            sortie_finale += entree[i]
        # ajout des majuscules
        elif i in majuscules:
            sortie_finale += sortie[h].upper()
            h += 1
        # ajout des lettres
        else:
            sortie_finale += sortie[h]
            h += 1
    print(sortie_finale)


# fonction de cécryptage ne modifiant que la partie de cryptage
def decryptage_vigenere(entree: str, cle: str):
    sortie = ""
    # retrait des caractères speciaux et des majuscules
    # nouvelle cle avec des minuscules uniquement
    nouvelle_cle = ""
    # remise en minuscule
    cle = cle.lower()
    for lettre in cle:
        # ajout des lettres uniquements
        if lettre in c.alphabet:
            nouvelle_cle += lettre
    # nouvelle entree avec uniquement des minuscules
    nouvelle_entree: str = ""
    majuscules: list = []
    caracteres_speciaux: list = []
    for a in range(len(entree)):
        # si c'est une majuscule
        if entree[a].isupper():
            majuscules.append(a)
            nouvelle_entree += entree[a].lower()
        # si c'est une minuscule
        elif entree[a] in c.alphabet:
            nouvelle_entree += entree[a]
        # si c'est un caractère spécial
        elif entree[a].lower() not in c.alphabet:
            caracteres_speciaux.append(a)
    # mise de l'entree et de la clé à la même taille
    while len(nouvelle_cle) < len(nouvelle_entree):
        nouvelle_cle += nouvelle_cle
    nouvelle_cle = nouvelle_cle[:len(nouvelle_entree)]
    # cryptage
    # pour chaque lettre minuscule de l'entree
    for i in range(len(nouvelle_entree)):
        # utilisation de la clé
        y: list = c.table_de_vigenere[c.alphabet.index(nouvelle_cle[i])]
        # recherche du caractère dans la ligne
        x: int = y.index(nouvelle_entree[i])
        # ajout de la lettre déchiffrée à la sortie
        sortie += c.table_de_vigenere[0][x]
    # remise en place des majuscules et des caractères speciaux
    sortie_finale: str = ""
    h: int = 0
    for i in range(len(entree)):
        # ajout des caractères spéciaux
        if i in caracteres_speciaux:
            sortie_finale += entree[i]
        # ajout des majuscules
        elif i in majuscules:
            sortie_finale += sortie[h].upper()
            h += 1
        # ajout des lettres
        else:
            sortie_finale += sortie[h]
            h += 1
    print(sortie_finale)
