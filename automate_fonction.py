"""
Author: Martin Calamel
Created: 2024-09-26
Description: fonction automate qui vérifie la structure grammatical d'une phrase 
TODO: 
"""

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
    alpha = "azertyuiopqsdfghjklmwxcvbn AZERTYUIOPQSDFGHJKLMWXCVBN."

    # élimine les caractère inconnue
    for i in phrase:
        if i in alpha:
            if i == ".":
                phrase_propre += " ."
            else:
                phrase_propre += i
    
    # transforme en une liste de mot
    liste_mot = phrase_propre.split()

    return liste_mot


def check_in_dico(dico: dict, key) -> bool:
    """
    vérifie la presence d'une clef dans un dictionnaire

    input: dictionnaire (dict), clef a verifier (pas de type précis)
    output: presence de la clef (bool)
    """
    return key in dico.keys()


def check_file(file_name: str) -> bool:
    """
    Fonction pour vérifier que le fichier est bien existant

    #input : nom du fichier a vérifier (str)
    #output : existence du fichier (bool)
    """
    if type(file_name) == str : 
        try:
            file_data = open(file_name)
            file_data.close()
            return True
        
        except FileNotFoundError:
            print("le fichier n'existe pas")
            return False

    else:
        print("mauvaise saisie du nom de fichier")
        return False

def read_file(file_name: str) -> list:
    """
    renvoi les données du fichier spécifier après avoir vérifier sont existence

    #input : nom du fichier (str)
    #output : données contenue dans le fichier (list)
    """
    if check_file(file_name):

        file = open(file_name, "r")
        content = file.read()
        content = content.split("\n") # sépare les element de content par ;
        data = [ i.split(";") for i in content]
        file.close()

        return data
    
def write_file(file_name: str, expression: str) -> None:
    """
    fonction qui ajoute une expression a la fin d'un fichier

    input: nom du fichier (str), expression a ajouter (str)
    output: rien
    """
    if check_file(file_name):
        file = open(file_name,"a")
        file.write(expression)
        file.close()

def make_dico_file(file: str) -> dict:
    """
    fait un dictionnaire a partir d'un fichier\n
    on part du principe que le fichier est sous le bon format pour travailler avec les dico

    input: nom du fichier où est stocker le dictionnaire (str)
    output: dictionnaire (dict)
    """

    data = read_file(file)
    dico = {i[0] : int(i[1]) for i in data}
    
    return dico

def add_to_dico_file(key: str, value: int, file: str) -> None:
    """
    fonction qui ajoute un ensemble clef valeur au fichier du dictionnaire

    input: clef (str), valeur (int), fichier du dictionnaire (str)
    output: rien
    """
    expression = "\n" + key + ";" + str(value)
    write_file(file, expression)

#### fonction automates

def changement_etats(etats: int, entree: int) -> int:
    """
    fonction qui donne l’état suivant a partir d'un état et d'une entrée

    input: état actuel (int), entree actuelle (int)
    output: état suivant (int)
    """
    suivant = matrice_etats[etats][entree]

    return suivant


def verif_phrase(phrase: str) -> int:
    """
    fonction principale de l'automate

    input: phrase a verifier (str)
    output: 0 si bien passer (int) 
    """
    # initialisation des variable local et global
    global dictionnaire
    
    if len(phrase) == 0:
        print("phrase incorrect")
    else : 
        liste_mots = format_phrase(phrase)
        etat = 0

        # verification pour chaque mots
        for i in liste_mots:
            if check_in_dico(dictionnaire, i): # si le mot existe dans le dictionnaire

                # changement d'état et gestion des cas de sortie 

                etat = changement_etats(etat, dictionnaire[i])
                if etat == 8:
                    print("phrase incorrect")
                    break
                if etat == 9:
                    print("phrase correct")
            else:
                # ajout du mot dans le dictionnaire selon la volonté de l'utilisateur
                print("Mot inexistant dans le dictionnaire :", i)
                choix = input("voulez-vous l'ajouter ? (Y/N) : ")

                if choix.upper() == "Y":

                    classe_mot = int(input("classe du mot:\n 0 = article\n 1 = adjectif\n 2 = Nom commun\n 3 = Nom Propre\n 4 = verbe\n>>>  "))
                    
                    add_to_dico_file(i, classe_mot, dico_file)
                    dictionnaire = make_dico_file(dico_file)
                    
                    verif_phrase(phrase)
                else:
                    print("mot inconnu, fin du programme")
                    break
        return 0


#### initialisation des variables

dico_file = "dictionnaire.txt"

dictionnaire = make_dico_file(dico_file)

matrice_etats = [[1, 8, 8, 4, 8, 8],
                 [8, 1, 2, 8, 8, 8],
                 [8, 2, 8, 8, 3, 8],
                 [5, 8, 8, 7, 8, 9],
                 [8, 8, 8, 8, 3, 8],
                 [8, 5, 6, 8, 8, 8],
                 [8, 6, 8, 8, 8, 9],
                 [8, 8, 8, 8, 8, 9]]



if __name__ == "__main__":

    # fonction write_file

    # write_file("dictionnaire.txt", "\nles;0")

    # fonction make_dico_file
    print(make_dico_file("dictionnaire.txt"))

    # fonction format_phrase

    print(format_phrase("Phrase avec; des truc!! pas beau du tout."))

    # fonction check_in_dico

    print("check_in_dico -> clef OK ", check_in_dico({0:1,2:3},0))
    print("check_in_dico -> clef OK ", check_in_dico({0:1,2:3},1))
    

    # fonction check_file

    print("check_file -> existence OK : ", check_file("dictionnaire.txt"))
    print("check_file -> existence NO : ", check_file("blabla.txt"))
    print("check_file -> mauvais format : ", check_file(12))
    print("\n\n")

    # fonction read_file

    print("read_file -> existence OK : ", read_file("dictionnaire.txt"))
    print("read_file -> existence NO : ", read_file("blabla.txt"))
    print("read_file -> mauvais format : ", read_file(12))
    print("\n\n")


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

    

