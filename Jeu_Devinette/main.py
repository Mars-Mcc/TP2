"""
Project TP2: Jeu Devinette
Un petit jeu de devinette de nombre
Mars McCullough groupe 404
2026-11-05
"""

import random


def game() :
    try_again = True
    while try_again == True:
        print("Bienvenue au JEU DEVINETTE!!! \n Règles: choisir un nombre minimum et maximum et deviner le nombre que l'ordinateur choisi \n(mettre le même numéro va résulter à un min de 1 et max de 100)")
        nombre_min = input("Saisir le nombre MINIMUM du JEU!")
        nombre_max = input("Saisir le nombre MAXIMUM du JEU")

        if nombre_min == nombre_max: #vérifica
            nombre_min = 1
            nombre_max = 100
        elif nombre_min > nombre_max:
            nombre_min = 1
            nombre_max = 100
        numero_special = random.randint(int(nombre_min), int(nombre_max))
        answer_wrong = True
        nombre_essai = 0

        while answer_wrong == True :
            essai = int(input("Deviner le nombre que je pense à ce moment"))
            if essai == numero_special :
                nombre_essai += 1
                print(f"BRAVO! vous avez gagné le jeu avec  {nombre_essai} essais")
                answer_wrong = False

            elif essai != numero_special :
                nombre_essai += 1
                print(f"OOPS! vous n'avez pas reussi, ressayer! ({nombre_essai} essais)")

        ressayer = input("voulez vous ressayer?(y ou n)")
        if ressayer == "y" :
            pass

        elif ressayer == "n" :
            print(f"Au revoir!")
            try_again = False

game()
