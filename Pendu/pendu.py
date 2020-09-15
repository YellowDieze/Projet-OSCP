"""Ceci est un jeu du pendu, l'ordinateur donne un mot aléatoire que
l'utilisateur devra trouver a l'aide de 5 chances. Un système de score existe
, moins l'utilisateur utilise de chance, plus il a de points
"""


from donnee import *
from fonction import *

#on vérifie la ^résence du fichier score
score_total= recup_scores()
#on demande le nom du joueur
utilisateur = recup_nom_utilisateur()
#on récupère le score du joueur si il a déja joué
if utilisateur not in score_total.keys():
    score_total[utilisateur]=0

jouer = True
trouvé = True
chance = 5
listeLettreUtilisé = list()


#le jeu se lance
while jouer:
    print("Joueur {0}: {1} point(s)".format(utilisateur, score_total[utilisateur]))
    print("Bienvenue sur le pendu")
    print("Le jeu va choisir un mot")
    #l'ordinateur choisis un mot
    mot= choisir_mot(liste_mots)
    #l'affiche en étant crypté
    mot_crypté=affichage(mot)
    print(mot_crypté)


    #Tant que le joueur n'a pas trouvé ou perdu, on continue de chercher le mot
    while trouvé:
        #copie la liste pour vérifier que le joueur a trouvé une lettre
        mot_cryptéAvant=copieListe(mot_crypté)
        #on test si la lettre est présente
        choixLettre=testerEntrer()
        #on vérifie que la lettre est utilisé ou non
        if lettreUtiliser(choixLettre,listeLettreUtilisé) == True:
            continue
        #on vérifie que la lettre est présente dans le mot
        mot_crypté=presence(choixLettre,mot,mot_crypté)

        #on vérifie si le joueur a trouvé ou non une lettre correct
        if mot_cryptéAvant == mot_crypté:
            chance =chanceRestante(chance)

        #si plus de chance alors perdu
        if chance < 1:
            print("Vous avez perdu !")
            break




        print(afficherMot(mot_crypté))
        #on vérifie que le mot est trouvé entièrement
        trouvé=motTrouver(mot_crypté)


    #si oui alors on compte le score et on passe à la suite
    if trouvé == False:
        print("Bravo, vous avez trouvé le mot")
        score_total[utilisateur]=chance+score_total[utilisateur]
    #on demande si le joueur veut rejouer
    print("Voulez-vous rejouer ? (y or n)")
    rejouer= input()
    rejouer=rejouer.lower()
    if rejouer== 'n':
        jouer= False
        print("Vous finissez la partie avec {0} points.".format(score_total[utilisateur]))
    if rejouer == 'y':
        trouvé = True
        listeLettreUtilisé = list()
        chance = 5
#on enregiste le score
enregistrer_scores(score_total)
