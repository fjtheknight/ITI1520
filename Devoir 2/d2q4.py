#Firas JRIBI
#O300084463

from random import randint as nAlea
def effectuezTest(operation):
    """fonction qui indique si l’élève a répondu correctement ou pas."""

    a = nAlea(0,9)
    b = nAlea(0,9)
    if operation == 0:
        bonneReponse = a + b
        reponseEleve = int(input(str(a)+" + "+str(b)+" = "))
        resultat = reponseEleve == bonneReponse
        if not resultat:
            print("Incorrect – la reponse est",bonneReponse)
    elif operation == 1:
        bonneReponse = a * b
        reponseEleve = int(input(str(a)+" * "+str(b)+" = "))
        resultat = reponseEleve == bonneReponse
        if not resultat:
            print("Incorrect – la reponse est",bonneReponse)
    return resultat

print("Ce logiciel va effectuez un test avec 10 questions ……")
compteur = 0
for i in range(0,10):
    operation = nAlea(0,1)
    resultat = effectuezTest(operation)
    if resultat:
        compteur += 1
print(compteur,"reponses correctes.")
if compteur > 6:
    print("Félicitations!")
else:
    print("Demandez à votre enseignant(e) de vous aider. ")
