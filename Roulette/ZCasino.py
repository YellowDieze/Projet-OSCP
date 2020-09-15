"""
Le but de ce programme est de recréer le jeu de la roulette, les règles sont simples :
    Le joueur possède un solde de départ, le joueur choisi un nombre de 0 à 49 et place une mise dessus.
    Le joueur gagne lorsque :
        _ la roulette tombe sur le même nombre que le joueur a choisit, gain = mise * 3 + mise
        _ la roulette tombesur la même couleur que le nombre du joueur (pair noir, impair rouge), gain = mise *0.5 + mise
    Le joueur perd lorsque il ne tombe ni sur le bon numéro, ni sur la bonne couleur, gain = 0
"""
import random
import math

solde = 100
jouer = True



#fonction qui donne la mise gagnée perdu ou gagné en fonction du résultat
def resultat(mise, choix, nbRoulette):
    if(choix==nbRoulette):
        mise=mise*3+mise
        affichage="Félicitation, vous êtes tombé sur le bon numéro"
        print(affichage.upper().center(70))
    if(choix%2==nbRoulette%2):
        mise=mise*0.5+mise
        affichage="vous n'avez pas le bon numéro mais vous tomber sur la bonne couleur"
        print(affichage.upper().center(70))
    else:
        mise=0
        affichage="vous avez perdu :("
        print(affichage.upper().center(70))
    return mise

#fonction qui fait tourner la roulette
def tournerRoulette():

    entier =random.randrange(50)
    print("La roulette à choisi le numéro :",entier)
    return entier




def choixEntier():
    print("choisir un nombre entre 0 et 49 :")
    #Tant que le joueur ne choisi pas un nombre valide, on continue de lui demander

    while True:
        choix = input()

        #On vérifie que le joueur choisi un entier
        try:
            choix=int(choix)

            if choix <0 and choix >49:
                print("La valeur n'est pas comprise entre 0 et 49, veuillez réessayer")

            if choix<0:
                print("La valeur n'est pas comprise entre 0 et 49, veuillez réessayer")

            #On sort de la boucle et on commence le jeu
            else:
                return choix
        #On renvoie l'erreur sinon
        except ValueError:
            print("La valeur n'est pas un entier")

        #On vérifier que l'entier est compris entre 0 et 49


def choixMise():
    global solde

    while True:
        #Le joueur choisi sa mise
        print("Votre solde est de :",solde,", Combien souhaitez-vous miser ?")
        mise=input()

        #on vérifier que la mise est un entier
        try:
            mise=int(mise)
            if mise <= 0 and mise > solde:
                print("Veuiller choisir une mise convenable")
            #On vérifie que le joueur a assez de solde pour miser
            if solde - mise < 0:
                print("Vous n'avez pas assez pour miser autant")
            if mise < 0:
                print("Veuillez miser une somme positive")

            else:

                solde=solde-mise
                print("Il vous reste :", solde,"comme solde")
                return mise

        except ValueError:
            print("La valeur n'est pas un entier")

        #Le joueur ne doit pas miser 0 ni plus que son solde disponible


"""
def rejouer():
    rejouer=input()
    return rejouer
"""

#Si le jouer n'a plus d'argent alors la partie est terminé
def perdu():

    if solde == 0:
        print("Vous n'avez plus d'argent, la partie est terminé !")
        return False
    else:
        return True

while jouer:

    choix=choixEntier() #Le joueur choisi le chiffre
    mise=choixMise() # Ensuite la mise

    res=tournerRoulette() # on fait tourner la roue
    solde =resultat(mise,choix,res) + solde #on vérifie si le joueur à gagner et on lui donne ses gains

    print("Votre solde est de :", solde)
    jouer = perdu()

    if solde > 0:

        print("Voulez vous rejouer (Y ou N)?")
        rejouer = input()


        if rejouer == 'N':
            print("A la prochaine fois :)")
            jouer = False

        if rejouer == 'Y':
            print("Super !")


        if rejouer !='N' and rejouer !='Y':
            print("Je n'ai pas compris, Veuillez entrer 'Y' ou 'N'")
