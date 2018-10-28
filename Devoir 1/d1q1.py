#Nom/Name : Firas JRIBI
#Numéro d'étudiant/Student number : 0300084463

"""
Ce programme permet de convertir en kilogrammes le poids de
livres et onces. Le programme va lire les deux valeurs à partir du clavier.
"""

print("Ce programme permet de convertir en kilogrammes le poids de livres et onces. Veuillez donner des valeurs à convertir.\n")

while True:

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            livres_string = input("Entrez le nombre de livres: ")
            livres_float = float(livres_string)
            if livres_float < 0:
                print("Veuillez entrer un nombre valide!")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
        else:
            break

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            onces_string = input('Entrez le nombre d\'onces: ')
            onces_float = float(onces_string)
            if onces_float < 0:
                print("Veuillez entrer un nombre valide!")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
        else:
            break

    kilo = 0.4536 * (livres_float + onces_float / 16)
    print("{0} livres et {1} onces équivalent à {2} kilogrammes".format(livres_string,onces_string,round(kilo,4)))
    print()

