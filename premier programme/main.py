
def demander_nom ():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est ton age? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print ("Vous devez saisir un nombre pour l'age.")
    return age_int

def afficher_information_personne(nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne (nom1,age1)
afficher_information_personne (nom2,age2)

"""print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans.")
print("L'année prochaine vous aurez " + str(age1 + 1) + " ans.")
print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans.")
print("L'année prochaine vous aurez " + str(age2 + 1) + " ans.")
print ("Merci, passez une bonne journée")
"""

