# Firas JRIBI
# 300084463

def sequenceMax(liste):
    """Fonction qui prend  une liste de
nombres et qui donne la longueur de la plus longue séquence d’éléments consécutifs égaux.

    Arguments:
        liste: liste de valeurs séparées par des virgules.
    Retours:
        Entier: longueur de la plus longue séquence d’éléments consécutifs égaux.

    """

    i = 0 #premier compteur pour la boucle while
    sequence_la_plus_longue = 1 #séquence la plus longue
    while len(liste) - i > sequence_la_plus_longue:#vérifier s'il y a plus d'éléments à parcourir que la longueur de la plus longue séquence, car inutile si la séquence est 5 et qu'il reste 5 ou moins éléments à parcourir
        #print("i:",liste[i])
        sequence_actuelle = 1 #séquence la plus logue actuelle
        j = i #compteur 2 pour comparer les deux séquences
        while j < len(liste)-1 and liste[j] == liste[j+1]: #si deux éléments consécutifs sont égaux
            #print("j:",liste[j])
            sequence_actuelle += 1 #incrémenter la séquence actuelle
            j += 1 #incrémenter comteur 2
        if sequence_actuelle > sequence_la_plus_longue: #si la nouvelle séquence est plus grande que l'ancienne
            sequence_la_plus_longue = sequence_actuelle #actualiser la valeur de la séquence la plus langue
        i = j + 1 #incrémenter le compteur 1
    return sequence_la_plus_longue #retourner la séquence d'éléments consécutifs égaux la plus longue

# Programme principal:
liste = eval(input("Veuillez entrer une liste de valeurs séparées par des virgules: ")) #demander à l'utilisateur de donner une liste de valeurs
print(sequenceMax(liste)) #afficher le résultat retourné par la fonction sequenceMax

