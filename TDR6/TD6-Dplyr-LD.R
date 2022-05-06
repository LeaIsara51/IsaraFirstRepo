##TD6 t3var avec dplyr
##OPEN22
##06/05/2022
##Cours Vincent Payet 

##Packages
library(dyplr)

##Importer les données dans un objet t3var.
t3var <- read.table("t3var.txt", header=TRUE, sep="\t")

##Identifier les noms des variables de ce jeu de données.
head(t3var)
names (t3var)

##Définir le contexte statistique (combien d’individus, de variables, types des variables).
dim(t3var)
ncol(t3var)
nrow(t3var)

##Sélectionner les individus 1, 10 et 20.
filter(t3var, sexe=="f")

##Sélectionner les femmes de plus de 170 cm. Combien sont-elles ?
filter(t3var, sexe=="f" & tai>170)
t3var %>%
  filter(sexe=="f") %>%
  filter(tai > 170) %>%
  nrow()

nrow(t3var[t3var$tai > 170 & t3var$sexe=="f, "])

t3var %>%
  filter(sexe=="f") %>%
  filter(tai > 170) %>%
  count()

##Pour les individus 10 à 20, donner toutes les variables sauf la première.
t3var %>%
  slice(10:20) %>% 
  select.at(!sexe) %>%
  rename_with( toupper)

##Sélectionner les femmes de taille supérieure à la taille moyenne des femmes, donner l’effectif de ce sous-groupe.
t3var %>%
  filter(sexe=="f") %>%
  filter(tai > mean(tai)) %>%
  count()

##Donner la moyenne des poids pour tous, puis par sexe.
t3var %>%
  summarise(moy=mean(poi))

t3var %>%
  select(!sexe) %>%
  summarise_all(mean)

t3var %>%
  groupe_by(sexe) %>%
  summarise_all(mean)

##Donner la variance des poids pour tous, 
#puis par sexe (la variance estimée ou de l’échantillon).
t3var %>%
  groupe_by(sexe) %>%
  summarise_all(sd)

#Select = choix de colonne 
t3var %>%
  select (sexe, tai)

#Group by + fonction : regroupement des lignes selon un critère 
t3var %>%
  group_by(sexe) %>%
  count()

## IMC 
t3var %>%
  mutate(taicm=tai/100) %>%
  mutate(imc=poi/taicm^2) %>%
  arrange(imc)
  
  

