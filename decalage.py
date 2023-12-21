import constante as c


def cryptage_decalage(message: str, valeur: int, etat: bool) -> None:
    entree: list = list(message.strip())
    print(entree)
    if valeur > 25:
        print("valeur trop élevée")
        exit(cryptage_decalage)
    if etat:
        valeur = -valeur
    for i in range(0, len(entree)):
        if entree[i] in c.echelle:
            entree[i] = c.echelle[(c.echelle.index(entree[i])) + valeur + len(c.alphabet)]
    sortie: str = "".join(entree)
    print(sortie)

