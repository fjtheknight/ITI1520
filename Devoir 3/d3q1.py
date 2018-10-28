# Firas JRIBI
# 300084463

def compte_pos(liste):
    """Fonction qui prend une liste de
nombres et qui donne le nombre d’éléments positifs (> 0) trouvés dans la liste.

    Arguments:
        liste: liste de valeurs séparées par des virgules.
    Retours:
        Entier: le nombre d'éléments positifs dans la liste.

    """
    elements_positifs = 0 #compteur d'éléments positifs
    for i in liste: #boucle pour parcourir la liste
        if i > 0: #si un élément est positif
            elements_positifs += 1 #on incrémente le compteur
    return elements_positifs #retourne le nombre d'éléments positifs

# Programme principal:
liste = eval(input("Veuillez entrer une liste de valeurs séparées par des virgules: ")) #demander à l'utilisateur de donner une liste de valeurs
print(compte_pos(liste)) #afficher le résultat retourné par la fonction compte_pos

