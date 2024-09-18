
#def demander_nom ():
#    reponse_nom = ""
#    while reponse_nom == "":
#        reponse_nom = input("Quel est ton nom? ")
#    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est ton age? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print ("Vous devez saisir un nombre pour l'age.")
    return age_int

def demander_taille(nom_personne):
    taille_float = 0
    while taille_float == 0:
        taille_str = input(nom_personne + " Vous mesurez combien? ")
        try:
            taille_float = float(taille_str)
        except ValueError:
            print ("Vous devez saisir un nombre pour votre taille.")
    return taille_float

def majeur(age):
    if age==17:
        print ("vous êtes presque majeur")
    elif age==18:
        print ("vous êtes tout juste majeur")
    elif 12 <= age < 18:
        print ("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print ("Vous êtes un bébé")
    elif age >60:
        print ("vous êtes sénior")   
    elif age<10:
        print ("vous êtes enfant")
    elif age > 18:
        print ("vous êtes majeur")
    else:
        print ("Vous êtes mineurs")


def afficher_information_personne(nom,age,taille=0):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    majeur(age)
    print("L'année prochaine vous aurez " + str(age + 1) + " ans.")
    if not taille == 0:
        print ("vous mesurez " + str(taille) + " m")
    

#nom1 = demander_nom()
#nom2 = demander_nom()

NB_PERSONNE = 1

for i in range(0, NB_PERSONNE):
    nom = "Personne " + str(i+1)
    age = demander_age(nom)
    taille = demander_taille(nom)
    afficher_information_personne (nom,age,taille)
#age2 = demander_age(nom2)


#afficher_information_personne (nom1,age1)
#afficher_information_personne (nom2,age2)

"""print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans.")
print("L'année prochaine vous aurez " + str(age1 + 1) + " ans.")
print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans.")
print("L'année prochaine vous aurez " + str(age2 + 1) + " ans.")
print ("Merci, passez une bonne journée")
"""

