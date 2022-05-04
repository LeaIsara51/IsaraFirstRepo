##2022/05/02
##VP
##Exemples R pour OPEN 2022 

x <- c(4, 5, 7, 4, 3, 9) 
#assignation = alt - 
x
x*2
mean(x, narm = TRUE)
# c'est une fonction 

y <- x*3+2
y[c(1,3)]# avoir que les 3 premieres valeurs 
y[y<20] #y inferieur à 20

plot(x, y)
hist(rnorm(2000))

read.table("Casino.csv", sep=";", header=TRUE, row.names = 1,dec =",")
read <- read.csv2("casino.csv", row.names = 1)

casino[1,2]
casino[casino$Couleur_voiture=="bleu" , ]

t3var <- read.table("t3var.txt", header=TRUE, sep="\t",stringsAsFactors = TRUE)

#install.packages("dplyr")
library(dplyr)
casino

read.table("casino.csv", sep=";", header=TRUE, row.names = 1,dec =",")
read <- read.csv2("casino.csv", row.names = 1)
casino
filter(casino, Couleur_voiture=="bleu")

Casino
select(casino, Score, Gain)

casino <- read.csv2("casino.csv", row.names = 1)

names(casino) # Savoir les colonnes 

#Sélectionner les lignes bleu et ne garder que les colonnes Score et Gain
#Sans dplyr

casino[casino$Couleur_voiture=="bleu" , 1:2 ]

#Avec dplyr 

filter(casino, Couleur_voiture=="bleu") 
select(casino, Score, Gain)

casiono_bleu <- filter(casino, Couleur_voiture=="bleu")

casino %>% # pipe = Ctrl Shift M %>% 
  filter(Couleur_voiture== "bleu") %>%
  select(Score, Gain) %>%
  mutate(rapport=Gain/Score)


