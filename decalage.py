import constante as c


def cryptage_decalage(message: str, valeur: int, etat: bool) -> None:
    entree: list = list(message.strip())
    print(entree)
    if etat:
        valeur = -valeur
    for i in range(0, len(entree)):
        if entree[i] in c.alphabet:
            entree[i] = c.alphabet[(c.alphabet.index(entree[i])) + valeur]
    sortie: str = "".join(entree)
    print(sortie)

