from donnee import *
import random
import pickle
import os

def chanceRestante(chance):
    """Donne les chances restantes à l'utilisateur"""
    chance -=1
    print("Vous avez perdu une vie, il vous reste",chance,"chances")
    return chance


def choisir_mot(liste):
    """Choisis aléatoirement un mot dans la liste"""
    aleatoire=random.randrange(len(liste))
    mot_choisi=liste[aleatoire]
    return mot_choisi

def affichage(mot):
    liste_underscore =list()
    for i in mot:
        liste_underscore.append("_")

#    liste_undescore = " ".join(liste_underscore)
    return liste_underscore

def presence(lettre, mot, liste_underscore):
    """vérifie la présence de la lettre dans le mot choisi,
    si oui alors la lettre est affiché"""
    y=0
    i=0
    t=0
    while i < len(liste_underscore):
        if liste_underscore[i]=="_":
            if mot[y]==lettre:
                liste_underscore[i]=lettre
                t=1
        y+=1
        i+=1
    if t==1:
        print("la lettre",lettre,"a été trouvé dans le mot")


    return liste_underscore

def testerEntrer():
    """teste si le caractère est valide ou non """

        choix=input("choisissez une lettre !\n")
        choix= choix.lower()
        if len(choix)>1 or not choix.isalpha():
            print(choix, "n'est pas un caractère valide, veuillez choisir une lettre")
            return testerEntrer()
        else:
            return choix

def motTrouver(mot):
    """vérifie si le mot a été trouvé"""

    i=0
    while i < len(mot):
        if mot[i] == "_":

             return True
        i+=1


    return False

def afficherMot(mot):
    """affiche le mot avec de beau espaces"""
    mot =" ".join(mot)
    return mot


def copieListe(liste):
    """copie une liste"""
    listeNew=list()
    listeNew.extend(liste)
    return listeNew


def lettreUtiliser(lettre, liste):
    """Cette fonction vérifie que l'utilisateur ne réutilise
     pas des lettres déja trouvé"""
    i=0
    while i < len(liste):
        if liste[i] == lettre:
            print("lettre déja utilisée")
            return True
        else:
            break

    liste.append(lettre)
    return False

def recup_scores():
    """Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire,
    soit l'objet dépicklé,
    soit un dictionnaire vide.

    On s'appuie sur nom_fichier_scores défini dans donnees.py"""

    if os.path.exists(nom_fichier_scores): # Le fichier existe
        # On le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores
    à enregistrer"""

    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
def recup_nom_utilisateur():
    """Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.

    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau"""

    nom_utilisateur = input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur
