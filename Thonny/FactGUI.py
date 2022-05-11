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
# coding: utf-8
 
from tkinter import * 
fenetre = Tk()
label = Label(fenetre, text="Entrer un nombre entier")
label.pack()
# entrée
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str(), width=30)
entree.pack()
fenetre.mainloop()
#bouton executer
from tkinter import *
def action() :
    try :
        Fact = 1
        N = 5
        if(N<0) :
            print("La valeur ne peut pas être négative")
            N = input
            # pourquoi input ?
        Résultat = ""
        # i = 1, car on le défnie juste en dessous dans range
        for i in range(1, 1) :
            Fact = Fact * i
        Resultat = str(Fact)
        print("La factorielle de " + str(N) + " est " + Resultat)
        #1
        print("La valeur de N est " + str(N))
        #2
        print(type(N))
        #3
        N = str(N)
        type(N)
        print (type(N))   
    except :
        print("Ne fonctionne pas avec du texte")
        N = input()
fenetre = Tk()
label = Label(fenetre, text="Entrez un nombre entier", bg="yellow")
label.pack()
value = StringVar()
value.set("Entrez un nombre entier")
entree = Entry(fenetre, textvariable=str(), width=30)
entree.pack()
bouton=Button(fenetre, text="Exécuter", command=action)
bouton.pack()
fenetre.mainloop()

