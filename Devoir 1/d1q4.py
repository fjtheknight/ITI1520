#Nom/Name : Firas JRIBI
#Numéro d'étudiant/Student number : 0300084463

"""
Ce programme permet de calculer le nombre minimal de pièces qu'un caissier peut
rendre.
"""

def numMonnaies(monnaie): #fonction pour calculer le nombre minimal de monnaies à rendre
    monnaie = int(monnaie * 100)
    return (monnaie // 25 + (monnaie % 25) // 10 + ((monnaie % 25)%10) // 5 + ((monnaie % 25) % 10) % 5 )

print("Ce programme permet de calculer le nombre minimal de pièces de monnaie qu'un caissier peut rendre.\n")

while True:

    while True: #vérifier que les valeurs saisies sont correctes
        try:
            donnee = input("Entrez le montant en dollars: ")
            if donnee[0] == "-" or len(donnee.rsplit('.')[-1]) > 2:
                print("Veuillez entrer un nombre valide!")
                continue
            montant = float (donnee)
            break
        except IndexError:
            print("Veuillez entrer un nombre valide!!")
            continue
        except ValueError:
            print("Veuillez entrer un nombre valide!!!")
            continue
        else:
            break

    print("Le nombre minimal de pièces que le caissier peut rendre est:", numMonnaies(montant))
    print()
