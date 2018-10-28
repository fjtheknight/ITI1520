#Firas JRIBI
#O300084463

from random import randint as nAlea
def effectuezTest(operation):
    """fonction qui teste l’élève avec l’une des deux opérations arithmétiques et retourne le nombre de bonnes réponses."""
    nomOperation = "multiplications"
    compteur = 0
    if operation == 0:
        nomOperation = "additions"
    print("SVP donnez les reponses aux "+nomOperation + " suivantes:",)
    for i in range(10):
        #a
        a = nAlea(0,9)
        b = nAlea(0,9)
        if operation == 0:
            #b
            bonneReponse = a + b
            #c
            reponseEleve = int(input(str(a)+" + "+str(b)+" = "))
            #d
            if reponseEleve == bonneReponse:
                compteur += 1
            else :
                print("Incorrect – la reponse est",bonneReponse)
        elif operation == 1:
            #b
            bonneReponse = a * b
            #c
            reponseEleve = int(input(str(a)+" * "+str(b)+" = "))
            #d
            if reponseEleve == bonneReponse:
                compteur += 1
            else :
                print("Incorrect – la reponse est",bonneReponse)
    return compteur


print("Ce logiciel va effectuez un test avec 10 questions ……")
operation = int(input("SVP choisisser l'operation 0) Addition 1) Multiplication (0 ou 1):\n"))

compteur = effectuezTest(operation)
print(compteur,"reponses correctes.")
if compteur > 6:
    print("Félicitations!")
else:
    print("Demandez à votre enseignant(e) de vous aider. ")
