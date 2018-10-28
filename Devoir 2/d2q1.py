#Firas JRIBI
#O300084463

def bmi(poids,taille):
    """fonction qui calcule l'IMC (BMI) à partir du poids et de la taille en mètre"""
    IMC = poids/taille**2
    return IMC

poids = float(input("SVP entre votre poids en kilogrammes: "))
taille = float(input("SVP entre votre taille en metres: "))
IMC = bmi(poids, taille)
print("Votre IMC est", IMC)
if IMC < 18.5:
    print("Maigreur")
elif IMC < 25:
    print("Poids idéal")
elif IMC < 30:
    print("Surpoids")
else :
    print("Obésité")
