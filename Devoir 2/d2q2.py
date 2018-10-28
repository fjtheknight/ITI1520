#Firas JRIBI
#O300084463

def affiche(a,b):
    """fonction qui affiche les entiers de a
à b, incluant a et b."""
    for i in range (a,b+1):
        print(i)

a = int(input("SVP donner la valeur de a: "))
b = int(input("SVP donner la valeur de b: "))
affiche(a,b)
