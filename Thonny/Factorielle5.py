# Quel type de structure itérative (boucle) allez-vous utiliser ? FOR ou WHILE ?
# FOR car fin de la boucle i=n
Fact = 1
N = 3
if N <= -1:
    print ("Erreur valeur négative")
    N=input()
Resultat = ""
#i = 1 pas util du coup 
for i in range (1, 4) :
    Fact = Fact * i
print(str(Fact))
Resultat = str(Fact)
print ("La factorielle de " + str(N) + " est " + Resultat)
print (N)
print (type (N))
#N = str(N)
#type (N)
#print (type (N))
#4. N = 8 ==> factorielle = 40320
#5. N = 0 ==> factorielle = 1
try :
    Fact = 1
    N = 6
    N = int(N)
    if N<= -1 :
        print("Erreur valeur négative")
        N = input()
    Resultat = ""
    #i = 1
    for i in range(1,6):
        Fact = Fact * i
    Resultat = str(Fact)
    print("La factorielle de " + str(N) + " est " + Resultat)
    print("la valeur de N est " + str(N))
    print(type(N))
except :
    print("Impossible d'insérer du texte, merci de mettre un nombre")
    N = input()
    