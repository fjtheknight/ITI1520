# Firas JRIBI
# 300084463

def sequenceDesDeux(liste):
    """Fonction qui prend une liste de
nombres et qui donne True s’il y a au moins une séquence de deux éléments consécutifs égaux, et False
dans le cas contraire.

    Arguments:
        liste: liste de valeurs séparées par des virgules.
    Retours:
        Booléen: s’il y a au moins une séquence de deux éléments consécutifs égaux.

    """

    i = 0 #compteur pour la boucle while
    deux_egaux = False #booleen supposant qu'au début les deux nombres ne sont pas égaux
    while i < len(liste)-1 and not deux_egaux:#boucle while avec deux conditions
        if liste[i] == liste[i+1]: #si deux éléments consécutifs sont égaux
            deux_egaux = True #changer le booleen de comparaison de False à True
            break #quitter la boucle immédiatement
        i += 1 #incrémenter le compteur
    return deux_egaux #retourner la valeur du booleen

# Programme principal:
liste = eval(input("Veuillez entrer une liste de valeurs séparées par des virgules: ")) #demander à l'utilisateur de donner une liste de valeurs
print(sequenceDesDeux(liste)) #afficher le résultat retourné par la fonction sequenceDesDeux

