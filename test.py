#Definir un tableau
#initialiser le TABLEAU
from random import Random, randrange

tab = [2, 4, 1, 45, 5, 59, 8]

#print(count(tab))
#test si le tab est valide 
#tab = [2, 4, 1, 45, 5, 17, 8] -> Ok
print("Je choisi au hazard entre 0 et " + str(len(tab) - 1))
print(tab)
pos_x_0 = randrange(0, len(tab), 1)

#recherchce des différent voisin
#choix de la solution initiale

x_0 = tab[pos_x_0]
str_post_x_0 = pos_x_0
str_post_x_0  = str(str_post_x_0) # Conversion de la postion en chaine pour affichage
str_x_0 = x_0
str_x_0 = str(str_x_0) # Conversion de la solution pour affichage

print('Solution x_0 choisie ' + str_x_0 + ' positionnée en ' + str_post_x_0)


# def voisinage(tab, element):


#     return max

#retourne tout la solution initiale et tout ses voisins direct 
# sous forme de tableau
def recup_voisinage(tab, pos_x_0):
    if pos_x_0 != 0 or pos_x_0 != len(tab)-1:
        new_tab = [tab[pos_x_0 - 1], tab[pos_x_0], tab[pos_x_0+1]]        
    elif pos_x_0 == 0:
        new_tab = [tab[pos_x_0], tab[2]]
    else:
        new_tab = [tab[pos_x_0], tab[pos_x_0 - 1]]

    return new_tab

def solution():
    return min(recup_voisinage(tab, pos_x_0))


print('La solution à notre algorithme de voisinage est : ' + str(solution()))
#tab = [2, 4, 1, 45, 5, 59, 8]