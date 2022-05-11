for i in range (1, 5):
    print(i*2)

for i in range (1, 5):
    print("calcul")
    print(i*2)

print("Fini")

t = "une phrase"
#on récupère la taille de la chaine
taille_t = len(t)

mess = "Python, c'est cool !"
#on récupère la taille de la chaine
taille = len(mess)
print("La chaine est de taille" + str(taille))

print("Quel est ton prénom?")
prenom = input()
print ("Bonjour" + prenom + "!")

print("Entrez un nombre")
nombre = input()
print(nombre)

print("entrer un nombre")
nombre = input()
print(nombre)
nombre2 = int(nombre) + 5
print(str(nombre2))

l1 = [1.2, 4.0, -5.1, 8.6, -3.7]
i = 2
# on récupère l'élément d'indice 2 dans une variable elt
elt = l1[i]
#on affiche dans la console et elt = élèment
print(elt)
#on affiche l'élément d'indice 0 dans la console
print(l1[0])

ch = "Une chaîne est une séquence"
premLettre = ch[0]
print("La première lettre est" + premLettre)

mot = "informatique"
debutMot = mot[0:4]
debutMot = mot[:4]
milieuMot = mot[5:7]
print("debutMot")

range (1, 5, 1)

if (condition1) :
    (bloc d'instructions 
