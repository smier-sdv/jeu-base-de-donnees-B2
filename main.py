from jeu import *

# variable running comme condition de boucle du jeu
running = True

# Fonction d'affichage du menu
    # afficher menu principal au lancement du jeu
    # sélection entre plusieurs options en utilisant des nombres
    # tant que infini
        # afficher les options numérotées
            # pour chaque option dans enumerate(options, start=1)
                # print(f"{i}. {option}")
        # demander un choix à l'utilisateur
        # appel de la fonction de vérification de validité du choix
        # si le choix est valide:
            # retourner le choix valide converti en int parce que sinon par défaut un input ça fait un string : int(choix)
        # afficher un message d'erreur


# fonction de vérification de la validité du choix
    # si le choix n'est pas isdigit()
        # retourner False
    # vérifier ou convertir un nombre en entier
    # si le choix est inférieur au minimum ou supérieur au maximum:
        # retourner False
    # retourner True


# Fonction gestion du choix de l'utilisateur    prend en paramètre la fonction d'affichage du menu de base
# si choix == 1:
    # Lancer le premier choix de la liste options
# si choix == 2: 
    # Lancer le 2ème choix
# même chose pour d'autres choix possibles