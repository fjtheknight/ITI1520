def print_paquet_deux_fois(main):
    '''(list)->None
    Affiche les éléments de la liste main deux fois.
    La première fois: ordonnée par couleur et après ca par valeur.
    La deuxième fois: ordonnée par valeurs.
    Precondition: main est un sub-set du paquet étrange.

    La fonction ne devrait pas changer l'ordre des éléments dans la liste main.
    Faîtes une copie de la liste et après ca appelez des fonctions de tri (sort).

    Exemple:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_paquet_deux_fois(a)
    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410
    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    copie_main = main.copy()
    copie_main.sort()
    for i in range(len(copie_main)-1):
        print(copie_main[i], end=" ")
    print(copie_main[i+1])
    copie_main.sort(key=lambda carte: carte%100)
    for i in range(len(copie_main)-1):
        print(copie_main[i], end=" ")
    print(copie_main[i+1])

def est_valide(cartes, joueur):
    '''(list of int, list of int)->bool
    La fonction retourne True si chaque carte dans la liste cartes est dans la main du joueur
    (dans la liste joueur).
    Sinon, elle affiche une message d'erreur et retourne False, comme dans les exemples suivantes.

    Precondition: cartes et joueur sont des sub-sets du paquet étrange.

    >>> est_valide([210,310],[201, 201, 210, 302, 311])
    310 n'est pas dans votre main. Entré invalide.
    False

    >>> est_valide([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for carte in cartes:
        if carte not in joueur:
            print(carte, "n'est pas dans votre main. Entré invalide.")
            return False
    return True

def est_valide_meme_valeur(cartes):
    '''(list of int)->True
    La fonction retourne True si les cartes dans la liste forment une combinaison valide
    de 2, 3 ou 4 carte de même valeur.
    Sinon elle retourne False. S'il n'y a pas assez des cartes pour former une combinaison valide,
    affiche un message, comme dans les exemples suivantes.

    Precondition: cartes est un sub-set du paquet étrange.

    Dans cette fonction, il ne faut pas convertir les cartes dans des chaines des caractères !!!

    >>> est_valide_meme_valeur([207, 107, 407])
    True
    >>> est_valide_meme_valeur([207, 107, 407])
    True
    >>> est_valide_meme_valeur([207, 107])
    Entré invalide. Les combinaisons valides de même valeur doit avoir au moins 2 cartes.??????????????????????? Il y a déjà 2 cartes!!!!!!!!!
    False
    '''
    if len(cartes)<2:
        print("Entré invalide. Les combinaisons valides de même valeur doit avoir au moins 2 cartes.")
        return False
    else:
        i = 0
        for i in range(len(cartes)-1):
            if cartes[i]%100 != cartes[i+1]%100:
                return False
    return True


def est_valide_seq(cartes):
    '''(list of int)->True
    La fonction retourne True si la liste cartes contient une séquence qui est une combinaison valide.
    Sinon, affiche un message d'erreur et retourne False, comme dans les exemples suivantes.

    Precondition: cartes est un sub-set du paquet étrange.

    Dans cette fonction, il ne faut pas convertir les cartes dans des chaines des caractères !!!

    >>> est_valide_seq([313, 311, 312])
    True
    >>> est_valide_seq([311, 312, 313, 414])
    Entré invalide. Les séquences valides doit être de même couleur.
    False
    >>> est_valide_seq([201, 202])
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    False
    >>> est_valide_seq([])
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    False
    '''

    if len(cartes)<3:
        print("Entré invalide. Les séquences valides doit avoir au moins 3 cartes.")
        return False
    else:
        cartes.sort()
        i = 0
        for i in range(len(cartes)-1):
            if cartes[i]+1 != cartes[i+1]:
                print("Entré invalide. Les séquences valides doit être de même couleur.")
                return False
    return True

def manche_dé_2_3_4_5_6(joueur):
    '''(list of int)->None
    Cette fonction joue une manche pour les valeurs 2, 3, 4, 5, ou 6 du dé.
    Precondition: joueur est un sub-set du paquet étrange.

    >>> manche_dé_2_3_4_5_6([401, 102, 403, 104, 203])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 102 103 104
    103 n'est pas dans votre main. Entré invalide.
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 403 203
    Voici la main, affichée de deux manières:
    102 104 401
    401 102 104
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  non

    >>> manche_dé_2_3_4_5_6([211, 412, 411, 103, 413])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 411 412 413
    Voici la main, affichée de deux manières:
    103 211
    103 211

    >>> manche_dé_2_3_4_5_6([211, 412, 411, 103, 413])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 411 412
    Entré invalide. Les séquences valides doit avoir au moins 3 cartes.
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  oui
    Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: 412 411 413
    Voici la main, affichée de deux manières:
    103 211
    103 211
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non)  non

    >>> manche_dé_2_3_4_5_6([401, 102, 403, 104, 203])
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) ssd
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) o
    Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) non
    '''
    condition = True
    reponse = ""
    while reponse.lower() not in ("oui","non") or not condition:
        reponse = input("Avez-vous une séquence de 3+ cartes de même couleur ou une combinaison de 2+ cartes de même valeur? (oui ou non) ")
        if reponse.lower() == "oui":
            cartes = [int(carte) for carte in (input("Quelle séquence de 3+ ou combinaison de 2+ carte de même valeur voulez-vous défausser? Entrez les cartes séparées par des espaces: ").split())]
            condition = est_valide(cartes,joueur) and (est_valide_meme_valeur(cartes) or est_valide_seq(cartes))
            if condition:
                for carte in cartes:
                    joueur.remove(carte)
                print("Voici la main, affichée de deux manières:")
                print_paquet_deux_fois(joueur)
                condition = False
        elif reponse.lower() == "non":
            return


manche_dé_2_3_4_5_6([211, 412, 411, 103, 413])
