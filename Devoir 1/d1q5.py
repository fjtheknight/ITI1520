#Nom/Name : Firas JRIBI
#Numéro d'étudiant/Student number : 0300084463

"""
Ce programme permet de convertir en secondes-lumière et en kilomètre les années-lumière. Le programme permet également de calculer la distance parcourue par un signal entre deux étoiles en passant par la terre.
"""

def anneesEnSecondes(annees): #fonction qui convertie les années_lumière en secondes_lumière
    return (annees * 365.26 * 24 * 60 * 60)

def secondesLumiereEnKm(secondes): #fonction qui convertie les secondes_lumière en kilomètres
    return (secondes * 300000)

def distanceEntreEtoiles(etoile1,etoile2): #fonction qui permet de calculer la distance que parcourt la lumière entre deux étoiles pasant par la Terre
     return (secondesLumiereEnKm(anneesEnSecondes(etoile1+etoile2)))

print("Ce programme permet de convertir en secondes-lumière et en kilomètre les années-lumière. Le programme permet également de calculer la distance parcourue par un signal entre deux étoiles en passant par la terre. Veuillez donner des valeurs à convertir.\n")

while True:

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            annees_lumiere = float(input("Entrez un nombre d’années-lumière: "))
            if annees_lumiere < 0:
                print("Veuillez entrer un nombre valide!")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
        else:
            break
    secondes_lumiere = round(anneesEnSecondes(annees_lumiere),1)
    print("Le nombre de secondes-lumière est",secondes_lumiere)
    kilometres = round(secondesLumiereEnKm(secondes_lumiere),1)
    print("La distance est",kilometres, "km.")

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            distance_premiere_etoile = float(input("Entrez la distance de la première étoile, en années-lumière: "))
            if distance_premiere_etoile < 0:
                print("Veuillez entrer un nombre valide!")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
        else:
            break

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            distance_deuxieme_etoile = float(input("Entrez la distance de la deuxième étoile, en années-lumière: "))
            if distance_deuxieme_etoile < 0:
                print("Veuillez entrer un nombre valide!")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue
        else:
            break

    distance = distanceEntreEtoiles(distance_premiere_etoile,distance_deuxieme_etoile)
    print("La distance entre les deux étoiles est",round(distance,1),"km.")
    print()

