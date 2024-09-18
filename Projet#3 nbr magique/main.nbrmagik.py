import random

NBR_MIN = 1
NBR_MAX = 10
NBR_MAGIK = random.randint(NBR_MIN,NBR_MAX)
nbr_saisie=0
NB_vie=4

def demander_nbr(NBR_MIN,NBR_MAX):
    nbr_saisie_int = 0
    while nbr_saisie_int == 0:
        nbr_saisie_str = input(f"Quel est le nombre magique ? (entre {NBR_MIN} et {NBR_MAX} )")
        try:
            nbr_saisie_int=int(nbr_saisie_str)
        except ValueError:
            print ("ERREUR: Vous devez saisir un nombre pour jouer. Réésayez.")
        else:
            if nbr_saisie_int<NBR_MIN or nbr_saisie_int>NBR_MAX:
                print (f"ERREUR: Vous devez saisir un nombre entre entre {NBR_MIN} et {NBR_MAX}. Réésayez.")
                nbr_saisie_int = 0
    return nbr_saisie_int

vies = NB_vie
while not nbr_saisie == NBR_MAGIK and vies>0:
    print (f"il vous reste {vies} vie(s)")
    nbr_saisie=demander_nbr(NBR_MIN,NBR_MAX)
    if nbr_saisie == NBR_MAGIK:
        print ("Vous avez trouvé le nombre magique!")
    elif nbr_saisie < NBR_MAGIK:
        print ("le nombre magique est plus grand")
        vies -= 1            
    else :
        print ("le nombre magique est plus petit")
        vies -= 1
if vies == 0:
        print (f"Vous avez perdu! le nombre magique était {NBR_MAGIK}")