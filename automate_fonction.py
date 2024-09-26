"""
Author: Martin Calamel
Created: 2024-09-26
Description: automate qui vérifie la structure grammatical d'une phrase 
TODO: dictionnaire en fichier:
        - fonction pour lire le fichier
        - fonction pour créer le dictionnaire
        - fonction pour modifier le dictionnaire
"""

#### initialisation des variables

dictionnaire = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 3,
"mange" : 4, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 4,"julie" : 3, "jean" : 3, "." : 5}

matrice_etats = [[1, 8, 8, 4, 8, 8],
                 [8, 1, 2, 8, 8, 8],
                 [8, 2, 8, 8, 3, 8],
                 [5, 8, 8, 7, 8, 9],
                 [8, 8, 8, 8, 3, 8],
                 [8, 5, 6, 8, 8, 8],
                 [8, 6, 8, 8, 8, 9],
                 [8, 8, 8, 8, 8, 9]]

#### fonction utiles

def format_phrase(phrase: str) -> list:
    """
    fonction qui nettoie une phrase afin qu'elle puisse être traiter par l'automate

    input: la phrase a traiter (str)
    output: liste des mots au bon format (list)
    """

    # définition des variables local
    phrase = phrase.lower()
    phrase_propre = ""
    alpha="azertyuiopqsdfghjklmwxcvbn AZERTYUIOPQSDFGHJKLMWXCVBN."

    # élimine les caractère inconnue
    for i in phrase:
        if i in alpha:
            if i == ".":
                phrase_propre += " ."
            else:
                phrase_propre+=i
    
    # transforme en une liste de mot
    liste_mot = phrase_propre.split()

    return liste_mot

def check_in_dico(dico: dict, key):
    """
    vérifie la presence d'une clef dans un dictionnaire

    input: dictionnaire (dict), clef a verifier (pas de type précis)
    output: presence de la clef (bool)
    """
    return key in dico.keys()

#### fonction automates

def changement_etats(etats: int, entree: int)->int:
    """
    fonction qui donne l’état suivant a partir d'un état et d'une entrée

    input: état actuel (int), entree actuelle (int)
    output: état suivant (int)
    """
    suivant=matrice_etats[etats][entree]

    return suivant


def verif_phrase(phrase: str) -> int:
    """
    fonction principale de l'automate

    input: phrase a verifier (str)
    output: 0 si bien passer (int) 
    """
    liste_mots=format_phrase(phrase)
    etat= 0
    for i in liste_mots:
        if check_in_dico(dictionnaire, i):
            etat = changement_etats(etat, dictionnaire[i])
            if etat == 8:
                print("phrase incorrect")
                break
            if etat == 9:
                print("phrase correct")
        else:
            print("Mot inexistant dans le dictionnaire :", i)
            choix = input("voulez-vous l'ajouter ? (Y/N) : ")
            if choix.upper() == "Y":
                classe_mot=int(input("classe du mot:\n 0 = article\n 1 = adjectif\n 2 = Nom commun\n 3 = Nom Propre\n 4 = verbe\n>>>  "))
                dictionnaire[i]=classe_mot
                verif_phrase(phrase)
    return 0



if __name__ == "__main__":

    # phrase qui devrait être correctes

    print("phrase OK")
    verif_phrase("le joli chat mange.")
    verif_phrase("le ,joli chat; dort.")
    verif_phrase("la grosse souris verte mange le joli petite chat blanc.")
    verif_phrase("la grosse souris verte mange jean.")
    verif_phrase("Jean dort.")
    verif_phrase("Jean mange Martin.")
    verif_phrase("Jean mange le chat.")
    verif_phrase("la verte souris grosse petit mange le bleu verte chat petite.")

    # phrase qui devrait être incorrect
    print("\n\nphrase NO")
    verif_phrase(".")
    verif_phrase("")
    verif_phrase("le joli chat joue")

    

