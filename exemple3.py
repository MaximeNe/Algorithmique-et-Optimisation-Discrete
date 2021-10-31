#!/usr/bin/env python3

souvegarde = {} # Permettera de construire la solution optimale par la suite

def h_max(longueur_base, largeur_base):
    """
    longueur_base = longeur maximale que peut avoir le mur
    largeur_base = largeur maximale que peut avoir le mur
    """

    # Conditions aux limites:
    if longueur_base == 0:
        return 0
    if largeur_base == 0:
        return 0


    # Trouver les brique qui peuvent convenir:
    B = []
    for brique in briques:
        # Si on a un brique moins longue et moins large que la base, alors elle pourrait convenir
        if brique[1] < largeur_base and brique[0] < longueur_base:
            B.append(brique)

    if len(B) == 0:
        return 0

    # Trouver la brique qui va maximiser l'equation de Bellman:
    i_max = 0
    val_max = 0
    for i, brique in enumerate(B):
        val = brique[2] + h_max((longueur_base//brique[0])*brique[0], brique[1])
        if val > val_max:
            val_max = val
            i_max = i

    # enregistrer le resultat dans souvegarde:
    if (longueur_base, largeur_base) in souvegarde:
        if souvegarde[(longueur_base, largeur_base)][1] < val_max:
            souvegarde[(longueur_base, largeur_base)] = (B[i_max], val_max)
        # Sinon laisser la solution precedente qui etait deja meilleure
    else:
        souvegarde[(longueur_base, largeur_base)] = (B[i_max], val_max)


    return val_max



if __name__ == "__main__":
    briques = ((10, 3, 5), (5, 6, 4), (1, 2, 3), (6, 4, 2), (7, 6, 5))
    n = len(briques)
    longueur_base = 100
    largeur_base = 10
    print("En prenant comme briques : ", briques)
    print("Et comme taille de fondations : ", (100, 10))
    print("h_max = ", h_max(longueur_base, largeur_base))
    print("En utilisant les briques suivantes (fondations en haut, ciel en bas)")
    long = longueur_base
    larg = largeur_base
    while (long, larg) in souvegarde:
        b = souvegarde[(long, larg)][0]
        print(b)
        long = (long//b[0])*b[0]
        larg = b[1]
