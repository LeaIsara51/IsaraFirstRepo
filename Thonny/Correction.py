#initialisations
Fact = 1
N = -1
#contrôle de saisie : boucler tant que N est strictement négatif
while (N < 0) :
    #récuperer la valeur de N
    ch_N = input("Quelle est la factorielle?\n")
    N = int(ch_N)
    #tester si N < 0
    if N < 0 :
        #écrire un message 
        print("Erreur valeur négative\n")
# tester si N > 0
if N > 0 :
    #boucler
    for i in range(1, N+1) :
        Fact = Fact * i
    #afficher le resultat
    print("La factorielle de " + str(N) + " est " + str(Fact))
else : # si N = 0
    print("La factorielle de " + str(N) + " est " + str(Fact))
