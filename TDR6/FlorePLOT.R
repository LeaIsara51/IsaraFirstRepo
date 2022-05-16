install.packages("car")
install.packages("FactoMineR")

library("car")
library("FactoMineR")

#On importe les 3 jeux de données.
FloreTot<-read.csv2("Flore.csv")
Microbio<-read.csv2("Microbio.csv")
Facteurs<-read.csv2("Facteurs.csv")

Facteurs

#On ne va s’intéresser qu’aux relevés de flore réalisés en 2011, vous allez donc extraire un sous-jeu de données

Flore<-FloreTot[FloreTot$Annee=="2011",-2]

#Dans un premier temps, on va calculer l’abondance totale de chaque communauté, que l’on appellera AbondanceAdv

Flore$AbondanceAdv<-rowSums(Flore[,c(2:90)])

#Puis on calcule la richesse en adventice de chaque communauté : RichesseAdv

Flore$RichesseAdv<-rowSums(Flore[,c(2:90)]>0)

#Enfin, on va calculer l’indice de Shannon de chaque communauté : ShannonAdv
Flore$ShannonAdv<-diversity(Flore[,c(2:90)],"shannon")

#On ne conserve finalement que ces 3 variables dans le tableau Flore

Flore<-Flore[,c(1,91:93)]

#on peut représenter l’abondance en adventices en fonction de la culture présente sur la parcelle.

ggplot(Flore,aes(x=Culture, y=AbondanceAdv))+geom_point()

#La richesse spécifique en adventices en fonction de l’IFT_Herbicide

ggplot(Flore,aes(x=IFT_Herbicide, y=RichesseAdv))+geom_point()

#Ou la richesse spécifique en micro-organismes du sol en fonction de la teneur en argile.

ggplot(Microbio,aes(x=Clay, y=RichesseMicro))+geom_point()



