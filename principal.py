"""
Author: Martin Calamel
Created: 2024-09-26
Description: programme principal pour les automates
TODO: 
"""

from automate_fonction import verif_phrase

choix="Y"
while choix.upper() == "Y":
    phrase = input("phrase a verifier : ")
    if verif_phrase(phrase):
        print("phrase correct")
    else :
        print("phrase incorrect")
    choix=input("voulez vous verifier une autre phrase (Y/N) : ")


